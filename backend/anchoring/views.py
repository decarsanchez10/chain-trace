from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from custody.models import CustodyEvent
from .models import AnchorTransaction
from .serializers import AnchorTransactionSerializer
from .tasks import anchor_pending_events

class AnchorTransactionListView(generics.ListAPIView):
    queryset = AnchorTransaction.objects.all().order_by('-created_at')
    serializer_class = AnchorTransactionSerializer

class PendingAnchorView(APIView):
    def get(self, request):
        pending_events = CustodyEvent.objects.filter(is_anchored=False)
        return Response({
            'pending_count': pending_events.count(),
            'pending_events': list(pending_events.values('id', 'payload_hash', 'timestamp'))
        })

class TriggerAnchorView(APIView):
    def post(self, request):
        anchored_count = anchor_pending_events()
        return Response({
            'message': f'Successfully processed anchoring for {anchored_count} pending event(s).',
            'anchored_count': anchored_count
        }, status=status.HTTP_200_OK)
