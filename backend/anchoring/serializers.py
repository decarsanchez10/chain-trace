from rest_framework import serializers
from .models import AnchorTransaction
from custody.serializers import CustodyEventSerializer

class AnchorTransactionSerializer(serializers.ModelSerializer):
    event_details = CustodyEventSerializer(source='event', read_only=True)

    class Meta:
        model = AnchorTransaction
        fields = [
            'id', 'event', 'event_details', 'txid', 'status',
            'network', 'op_return_payload', 'block_height',
            'block_hash', 'explorer_url', 'created_at', 'updated_at'
        ]
