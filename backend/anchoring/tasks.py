from custody.models import CustodyEvent
from .models import AnchorTransaction
from .bch_client import BCHClient

def anchor_pending_events():
    """Background task to anchor un-anchored custody events on BCH."""
    pending_events = CustodyEvent.objects.filter(is_anchored=False)
    client = BCHClient()
    for event in pending_events:
        txid = client.broadcast_op_return(event.payload_hash)
        AnchorTransaction.objects.create(
            event=event,
            txid=txid,
            status='CONFIRMED'
        )
        event.is_anchored = True
        event.save()
