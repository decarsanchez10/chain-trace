from rest_framework import serializers
from .models import Asset, Handler, CustodyEvent

class HandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handler
        fields = ['id', 'name', 'role', 'badge_id', 'wallet_address', 'email', 'created_at']

class AssetSerializer(serializers.ModelSerializer):
    event_count = serializers.SerializerMethodField()

    class Meta:
        model = Asset
        fields = ['id', 'asset_uid', 'name', 'description', 'category', 'status', 'owner_wallet_address', 'event_count', 'created_at']

    def get_event_count(self, obj):
        return obj.events.count()

class CustodyEventSerializer(serializers.ModelSerializer):
    asset_details = AssetSerializer(source='asset', read_only=True)
    handler_details = HandlerSerializer(source='handler', read_only=True)
    txid = serializers.SerializerMethodField()

    class Meta:
        model = CustodyEvent
        fields = [
            'id', 'asset', 'asset_details', 'handler', 'handler_details',
            'timestamp', 'location', 'device_id', 'reed_switch_triggered',
            'accel_shock_detected', 'tamper_status', 'payload_hash',
            'signature', 'raw_payload', 'is_anchored', 'txid', 'created_at'
        ]
        read_only_fields = ['payload_hash', 'tamper_status', 'is_anchored', 'created_at']

    def get_txid(self, obj):
        tx = getattr(obj, 'anchor_tx', None)
        return tx.txid if tx else None

class ScanIngestionSerializer(serializers.Serializer):
    asset_uid = serializers.CharField(max_length=100)
    asset_name = serializers.CharField(max_length=255, required=False, default="Scanned Asset")
    handler_badge_id = serializers.CharField(max_length=100, required=False, default="DEFAULT_HANDLER")
    handler_name = serializers.CharField(max_length=255, required=False, default="Default Handler")
    timestamp = serializers.DateTimeField(required=False)
    location = serializers.CharField(max_length=255, required=False, default="Checkpoint Alpha")
    device_id = serializers.CharField(max_length=100, required=False, default="ESP32-NODE-01")
    reed_switch_triggered = serializers.BooleanField(required=False, default=False)
    accel_shock_detected = serializers.BooleanField(required=False, default=False)
    signature = serializers.CharField(required=False, allow_blank=True, default="")
    auto_anchor = serializers.BooleanField(required=False, default=True)

