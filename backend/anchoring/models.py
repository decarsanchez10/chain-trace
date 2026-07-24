from django.db import models
from custody.models import CustodyEvent

class AnchorTransaction(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('FAILED', 'Failed'),
    ]
    event = models.OneToOneField(CustodyEvent, on_delete=models.CASCADE, related_name='anchor_tx')
    txid = models.CharField(max_length=64, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TX {self.txid} ({self.status})"
