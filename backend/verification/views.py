from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from custody.models import CustodyEvent

class VerifyEventView(APIView):
    def get(self, request, event_id):
        try:
            event = CustodyEvent.objects.get(id=event_id)
            tx = getattr(event, 'anchor_tx', None)
            return Response({
                'event_id': event.id,
                'payload_hash': event.payload_hash,
                'is_anchored': event.is_anchored,
                'txid': tx.txid if tx else None,
                'verified': event.is_anchored and tx is not None
            })
        except CustodyEvent.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
