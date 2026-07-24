from django.db import models

class Handler(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    public_key = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Asset(models.Model):
    asset_uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.asset_uid})"

class CustodyEvent(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='events')
    handler = models.ForeignKey(Handler, on_delete=models.CASCADE, related_name='scans')
    timestamp = models.DateTimeField()
    payload_hash = models.CharField(max_length=64)
    signature = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    is_anchored = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event {self.id} - {self.asset.asset_uid}"
