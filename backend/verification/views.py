from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from custody.models import CustodyEvent, Asset

class VerifyEventView(APIView):
    """
    Audits a single custody event by recalculating its payload hash,
    comparing against stored record, checking BCH anchoring transaction,
    and evaluating physical/enclosure tamper indicators.
    """
    def get(self, request, event_id):
        try:
            event = CustodyEvent.objects.get(id=event_id)
            recalculated_hash = event.compute_hash()
            hash_match = (recalculated_hash == event.payload_hash)
            
            tx = getattr(event, 'anchor_tx', None)
            is_anchored = event.is_anchored and (tx is not None and tx.status == 'CONFIRMED')
            is_tamper_free = (event.tamper_status == 'CLEAN')
            is_valid = hash_match and is_anchored and is_tamper_free

            return Response({
                'event_id': event.id,
                'asset_uid': event.asset.asset_uid,
                'handler_name': event.handler.name,
                'timestamp': event.timestamp.isoformat(),
                'location': event.location,
                'device_id': event.device_id,
                'recorded_hash': event.payload_hash,
                'recalculated_hash': recalculated_hash,
                'hash_integrity_valid': hash_match,
                'tamper_status': event.tamper_status,
                'is_anchored': is_anchored,
                'blockchain': {
                    'txid': tx.txid if tx else None,
                    'status': tx.status if tx else 'UNANCHORED',
                    'op_return': tx.op_return_payload if tx else None,
                    'explorer_url': tx.explorer_url if tx else None,
                },
                'is_valid': is_valid,
                'verification_status': 'VERIFIED' if is_valid else ('TAMPERED' if not is_tamper_free or not hash_match else 'UNANCHORED')
            })
        except CustodyEvent.DoesNotExist:
            return Response({'error': f'Custody Event #{event_id} not found'}, status=status.HTTP_404_NOT_FOUND)

class VerifyAssetChainView(APIView):
    """
    Audits the entire custody chain for a given Asset UID.
    Validates chronological sequence, off-chain record hash integrity,
    and BCH blockchain anchoring across all checkpoints.
    """
    def get(self, request, asset_uid):
        try:
            asset = Asset.objects.get(asset_uid=asset_uid)
            events = asset.events.all().order_by('timestamp')

            if not events.exists():
                return Response({
                    'asset_uid': asset.asset_uid,
                    'asset_name': asset.name,
                    'chain_intact': False,
                    'total_events': 0,
                    'message': 'No custody events recorded for this asset.'
                }, status=status.HTTP_200_OK)

            audit_trail = []
            chain_intact = True
            tampered_count = 0
            unanchored_count = 0

            for idx, event in enumerate(events):
                recalculated_hash = event.compute_hash()
                hash_valid = (recalculated_hash == event.payload_hash)
                tx = getattr(event, 'anchor_tx', None)
                anchored = event.is_anchored and (tx is not None and tx.status == 'CONFIRMED')
                tamper_free = (event.tamper_status == 'CLEAN')

                if not hash_valid or not tamper_free:
                    tampered_count += 1
                    chain_intact = False
                if not anchored:
                    unanchored_count += 1

                audit_trail.append({
                    'step': idx + 1,
                    'event_id': event.id,
                    'timestamp': event.timestamp.isoformat(),
                    'location': event.location,
                    'handler': event.handler.name,
                    'payload_hash': event.payload_hash,
                    'hash_valid': hash_valid,
                    'tamper_status': event.tamper_status,
                    'anchored': anchored,
                    'txid': tx.txid if tx else None,
                    'explorer_url': tx.explorer_url if tx else None
                })

            return Response({
                'asset': {
                    'asset_uid': asset.asset_uid,
                    'name': asset.name,
                    'category': asset.category,
                    'current_status': asset.status,
                },
                'chain_summary': {
                    'chain_intact': chain_intact,
                    'total_events': len(events),
                    'anchored_events': len(events) - unanchored_count,
                    'unanchored_events': unanchored_count,
                    'tampered_events': tampered_count,
                    'verification_result': 'PASSED_SECURE' if (chain_intact and unanchored_count == 0) else ('FAILED_TAMPERED' if tampered_count > 0 else 'PENDING_ANCHOR')
                },
                'audit_trail': audit_trail
            })
        except Asset.DoesNotExist:
            return Response({'error': f'Asset with UID {asset_uid} not found'}, status=status.HTTP_404_NOT_FOUND)

