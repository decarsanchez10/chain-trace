from django.db import models
from custody.models import CustodyEvent

class AnchorTransaction(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Broadcast'),
        ('CONFIRMED', 'Confirmed on Blockchain'),
        ('FAILED', 'Broadcast Failed'),
    ]

    event = models.OneToOneField(CustodyEvent, on_delete=models.CASCADE, related_name='anchor_tx')
    txid = models.CharField(max_length=64, unique=True, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    network = models.CharField(max_length=50, default='chipnet')
    op_return_payload = models.CharField(max_length=255, blank=True)
    block_height = models.IntegerField(null=True, blank=True)
    block_hash = models.CharField(max_length=64, blank=True, null=True)
    explorer_url = models.URLField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.explorer_url and self.txid:
            if self.network == 'chipnet':
                self.explorer_url = f"https://chipnet.imaginary.cash/tx/{self.txid}"
            else:
                self.explorer_url = f"https://blockchair.com/bitcoin-cash/transaction/{self.txid}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"TX {self.txid[:16]}... ({self.status})"

