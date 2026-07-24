from rest_framework import serializers
from .models import Asset, Handler, CustodyEvent

class HandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handler
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class CustodyEventSerializer(serializers.ModelSerializer):
    asset_details = AssetSerializer(source='asset', read_only=True)
    handler_details = HandlerSerializer(source='handler', read_only=True)

    class Meta:
        model = CustodyEvent
        fields = '__all__'
