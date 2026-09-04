from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone

from custody.models import Asset, Handler, CustodyEvent
from anchoring.tasks import anchor_pending_events

class Command(BaseCommand):
    help = 'Seeds database with realistic sample assets, handlers, scans, tamper alerts, and anchored BCH transactions.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Clearing old sample custody data...'))
        CustodyEvent.objects.all().delete()
        Asset.objects.all().delete()
        Handler.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating Handlers...'))
        h1 = Handler.objects.create(
            name="Alice Vance", role="Logistics Officer", badge_id="HD-1001",
            wallet_address="bitcoincash:qpm2q58vud305v62vch25w0tqv2n92nvks0uhuh2v5",
            email="alice@chaintrace.io"
        )
        h2 = Handler.objects.create(
            name="Bob Miller", role="Transit Driver", badge_id="HD-1002",
            wallet_address="bitcoincash:qr63q58vud305v62vch25w0tqv2n92nvks9y5pkwy3",
            email="bob@chaintrace.io"
        )
        h3 = Handler.objects.create(
            name="Carol Danvers", role="Customs Inspector", badge_id="HD-1003",
            wallet_address="bitcoincash:qp03q58vud305v62vch25w0tqv2n92nvks74hk3pq8",
            email="carol@chaintrace.io"
        )

        self.stdout.write(self.style.SUCCESS('Creating Assets...'))
        a1 = Asset.objects.create(
            asset_uid="MED-VAX-98214",
            name="Temp-Controlled Vaccine Vault #402",
            description="Ultra-cold storage bio-medical container holding mRNA vaccines.",
            category="Pharmaceuticals",
            status="IN_TRANSIT",
            owner_wallet_address="bitcoincash:qpm2q58vud305v62vch25w0tqv2n92nvks0uhuh2v5"
        )
        a2 = Asset.objects.create(
            asset_uid="SEC-HSM-55109",
            name="Hardware Security Module Container",
            description="High-security sealed container housing bank cryptographic key hardware.",
            category="Electronics",
            status="FLAGGED_TAMPERED",
            owner_wallet_address="bitcoincash:qr63q58vud305v62vch25w0tqv2n92nvks9y5pkwy3"
        )

        now = timezone.now()

        self.stdout.write(self.style.SUCCESS('Creating Custody Events for MED-VAX-98214...'))
        e1 = CustodyEvent.objects.create(
            asset=a1, handler=h1, timestamp=now - timedelta(hours=12),
            location="Pharma Warehouse A - Dispatch", device_id="ESP32-NODE-01",
            reed_switch_triggered=False, accel_shock_detected=False
        )
        e2 = CustodyEvent.objects.create(
            asset=a1, handler=h2, timestamp=now - timedelta(hours=6),
            location="Transit Checkpoint North - Port 4", device_id="ESP32-NODE-02",
            reed_switch_triggered=False, accel_shock_detected=False
        )

        self.stdout.write(self.style.SUCCESS('Creating Custody Events with Tamper Flag for SEC-HSM-55109...'))
        e3 = CustodyEvent.objects.create(
            asset=a2, handler=h1, timestamp=now - timedelta(hours=18),
            location="Bank Vault Storage - Origin", device_id="ESP32-NODE-01",
            reed_switch_triggered=False, accel_shock_detected=False
        )
        e4 = CustodyEvent.objects.create(
            asset=a2, handler=h3, timestamp=now - timedelta(hours=2),
            location="Customs Inspection Station Bravo", device_id="ESP32-NODE-03",
            reed_switch_triggered=True, accel_shock_detected=True
        )

        self.stdout.write(self.style.SUCCESS('Anchoring events on Bitcoin Cash...'))
        anchored_count = anchor_pending_events()
        
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded database and anchored {anchored_count} event(s) on BCH!'))
