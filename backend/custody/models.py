import hashlib
import json
from django.db import models

class Handler(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100, default='Custodian')
    badge_id = models.CharField(max_length=100, blank=True, null=True, unique=True)
    wallet_address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role})"

class Asset(models.Model):
    STATUS_CHOICES = [
        ('IN_TRANSIT', 'In Transit'),
        ('STORED', 'Stored / In Warehouse'),
        ('DELIVERED', 'Delivered'),
        ('FLAGGED_TAMPERED', 'Flagged as Tampered'),
    ]

    asset_uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, default='General Cargo')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='IN_TRANSIT')
    owner_wallet_address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.asset_uid})"

class CustodyEvent(models.Model):
    TAMPER_CHOICES = [
        ('CLEAN', 'No Tampering Detected'),
        ('TAMPERED_REED', 'Enclosure Breached (Reed Switch)'),
        ('TAMPERED_SHOCK', 'Physical Impact Detected (MPU6050 Accelerometer)'),
        ('TAMPERED_MULTIPLE', 'Multiple Tamper Signals Detected'),
    ]

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='events')
    handler = models.ForeignKey(Handler, on_delete=models.CASCADE, related_name='scans')
    timestamp = models.DateTimeField()
    location = models.CharField(max_length=255, default='Checkpoint Alpha')
    device_id = models.CharField(max_length=100, default='ESP32-NODE-01')
    
    reed_switch_triggered = models.BooleanField(default=False)
    accel_shock_detected = models.BooleanField(default=False)
    tamper_status = models.CharField(max_length=30, choices=TAMPER_CHOICES, default='CLEAN')

    payload_hash = models.CharField(max_length=64, db_index=True)
    signature = models.TextField(blank=True, null=True)
    raw_payload = models.JSONField(blank=True, null=True)
    is_anchored = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def compute_hash(self) -> str:
        """Calculates deterministic SHA-256 hash of event telemetry."""
        if hasattr(self.timestamp, 'isoformat'):
            ts_str = self.timestamp.isoformat().replace('+00:00', 'Z')
        else:
            ts_str = str(self.timestamp).replace('+00:00', 'Z')

        payload = {
            'asset_uid': self.asset.asset_uid,
            'handler_id': self.handler.id,
            'timestamp': ts_str,
            'location': self.location,
            'device_id': self.device_id,
            'reed_switch_triggered': self.reed_switch_triggered,
            'accel_shock_detected': self.accel_shock_detected,
        }
        encoded = json.dumps(payload, sort_keys=True).encode('utf-8')
        return hashlib.sha256(encoded).hexdigest()

    def evaluate_tamper_status(self):
        if self.reed_switch_triggered and self.accel_shock_detected:
            self.tamper_status = 'TAMPERED_MULTIPLE'
        elif self.reed_switch_triggered:
            self.tamper_status = 'TAMPERED_REED'
        elif self.accel_shock_detected:
            self.tamper_status = 'TAMPERED_SHOCK'
        else:
            self.tamper_status = 'CLEAN'

    def save(self, *args, **kwargs):
        self.evaluate_tamper_status()
        super().save(*args, **kwargs)
        if not self.payload_hash or self.payload_hash != self.compute_hash():
            self.payload_hash = self.compute_hash()
            super().save(update_fields=['payload_hash'])


    def __str__(self):
        return f"Event #{self.id} - {self.asset.asset_uid} [{self.tamper_status}]"

