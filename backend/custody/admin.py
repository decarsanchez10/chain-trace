from django.contrib import admin
from .models import Asset, Handler, CustodyEvent

@admin.register(Handler)
class HandlerAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'badge_id', 'wallet_address', 'created_at')
    search_fields = ('name', 'badge_id', 'wallet_address')

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_uid', 'name', 'category', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('asset_uid', 'name')

@admin.register(CustodyEvent)
class CustodyEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset', 'handler', 'timestamp', 'is_anchored')
