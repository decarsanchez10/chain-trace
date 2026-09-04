from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from custody.models import Asset, Handler, CustodyEvent
from anchoring.models import AnchorTransaction
from anchoring.tasks import anchor_pending_events

class ChainTraceBackendAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.handler = Handler.objects.create(
            name="Test Custodian",
            role="Inspector",
            badge_id="TEST-BADGE-01"
        )
        self.asset = Asset.objects.create(
            asset_uid="TEST-TAG-9999",
            name="Test Supply Container",
            category="Test Cargo"
        )

    def test_receive_scan_ingestion(self):
        url = reverse('receive-scan')
        payload = {
            'asset_uid': 'TEST-TAG-9999',
            'handler_badge_id': 'TEST-BADGE-01',
            'location': 'Test Checkpoint Delta',
            'device_id': 'ESP32-TEST-NODE',
            'reed_switch_triggered': False,
            'accel_shock_detected': False,
            'auto_anchor': True
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('payload_hash', response.data)
        self.assertTrue(response.data['is_anchored'])
        self.assertIsNotNone(response.data['txid'])

    def test_tamper_detection_on_scan(self):
        url = reverse('receive-scan')
        payload = {
            'asset_uid': 'TEST-TAG-9999',
            'handler_badge_id': 'TEST-BADGE-01',
            'reed_switch_triggered': True,
            'accel_shock_detected': True,
            'auto_anchor': False
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['tamper_status'], 'TAMPERED_MULTIPLE')
        
        # Verify asset status updated to FLAGGED_TAMPERED
        self.asset.refresh_from_db()
        self.assertEqual(self.asset.status, 'FLAGGED_TAMPERED')

    def test_verification_single_event(self):
        event = CustodyEvent.objects.create(
            asset=self.asset,
            handler=self.handler,
            timestamp='2026-09-04T12:00:00Z',
            location='Origin Station',
            device_id='ESP32-NODE-01'
        )
        anchor_pending_events()

        url = reverse('verify-event', kwargs={'event_id': event.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['hash_integrity_valid'])
        self.assertTrue(response.data['is_anchored'])
        self.assertTrue(response.data['is_valid'])

    def test_verification_asset_chain(self):
        e1 = CustodyEvent.objects.create(
            asset=self.asset, handler=self.handler,
            timestamp='2026-09-04T10:00:00Z', location='Station 1'
        )
        e2 = CustodyEvent.objects.create(
            asset=self.asset, handler=self.handler,
            timestamp='2026-09-04T14:00:00Z', location='Station 2'
        )
        anchor_pending_events()

        url = reverse('verify-asset-chain', kwargs={'asset_uid': self.asset.asset_uid})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['chain_summary']['chain_intact'])
        self.assertEqual(response.data['chain_summary']['total_events'], 2)
        self.assertEqual(response.data['chain_summary']['verification_result'], 'PASSED_SECURE')
