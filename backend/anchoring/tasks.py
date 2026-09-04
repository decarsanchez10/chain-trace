from custody.models import CustodyEvent
from .models import AnchorTransaction
from .bch_client import BCHClient

def anchor_pending_events():
    """Background task to anchor un-anchored custody events on BCH."""
    pending_events = CustodyEvent.objects.filter(is_anchored=False)
    client = BCHClient()
    anchored_count = 0

    for event in pending_events:
        res = client.broadcast_op_return(event.payload_hash)
        
        AnchorTransaction.objects.update_or_create(
            event=event,
            defaults={
                'txid': res['txid'],
                'status': res['status'],
                'network': res['network'],
                'op_return_payload': res['op_return_payload'],
            }
        )
        event.is_anchored = True
        event.save(update_fields=['is_anchored'])
        anchored_count += 1

    return anchored_count

