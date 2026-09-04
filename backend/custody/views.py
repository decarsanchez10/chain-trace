from django.utils import timezone
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Asset, Handler, CustodyEvent
from .serializers import (
    AssetSerializer, HandlerSerializer, CustodyEventSerializer, ScanIngestionSerializer
)
from anchoring.tasks import anchor_pending_events

class HandlerViewSet(viewsets.ModelViewSet):
    queryset = Handler.objects.all().order_by('-created_at')
    serializer_class = HandlerSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('-created_at')
    serializer_class = AssetSerializer
    lookup_field = 'asset_uid'

class CustodyEventListCreateView(generics.ListCreateAPIView):
    queryset = CustodyEvent.objects.all().order_by('-timestamp')
    serializer_class = CustodyEventSerializer

class AssetDetailView(generics.RetrieveAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    lookup_field = 'asset_uid'

class AssetHistoryView(APIView):
    def get(self, request, asset_uid):
        try:
            asset = Asset.objects.get(asset_uid=asset_uid)
            events = asset.events.all().order_by('-timestamp')
            serializer = CustodyEventSerializer(events, many=True)
            asset_data = AssetSerializer(asset).data
            return Response({
                'asset': asset_data,
                'events_count': events.count(),
                'has_tamper_flag': events.filter(tamper_status__startswith='TAMPERED').exists(),
                'events': serializer.data
            })
        except Asset.DoesNotExist:
            return Response({'error': f'Asset with UID {asset_uid} not found'}, status=status.HTTP_404_NOT_FOUND)

class ReceiveScanView(APIView):
    """
    Ingest hardware scan payload from ESP32 node or web interface.
    Autocreates assets/handlers if necessary, calculates payload hash,
    and optionally triggers BCH anchoring.
    """
    def post(self, request):
        serializer = ScanIngestionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        
        # 1. Resolve or create Asset
        asset, _ = Asset.objects.get_or_create(
            asset_uid=data['asset_uid'],
            defaults={'name': data.get('asset_name', f"Asset {data['asset_uid']}")}
        )

        # Update asset status if tampered
        reed = data.get('reed_switch_triggered', False)
        shock = data.get('accel_shock_detected', False)
        if reed or shock:
            asset.status = 'FLAGGED_TAMPERED'
            asset.save()

        # 2. Resolve or create Handler
        handler, _ = Handler.objects.get_or_create(
            badge_id=data.get('handler_badge_id', 'DEFAULT_HANDLER'),
            defaults={'name': data.get('handler_name', 'Default Handler')}
        )

        # 3. Create Custody Event
        scan_time = data.get('timestamp') or timezone.now()
        event = CustodyEvent(
            asset=asset,
            handler=handler,
            timestamp=scan_time,
            location=data.get('location', 'Checkpoint Alpha'),
            device_id=data.get('device_id', 'ESP32-NODE-01'),
            reed_switch_triggered=reed,
            accel_shock_detected=shock,
            signature=data.get('signature', ''),
            raw_payload=request.data,
        )
        event.save() # Computes hash & tamper_status automatically

        # 4. Trigger auto-anchoring if requested
        if data.get('auto_anchor', True):
            anchor_pending_events()
            event.refresh_from_db()

        return Response(CustodyEventSerializer(event).data, status=status.HTTP_201_CREATED)

