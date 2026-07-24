from django.contrib import admin
from .models import Asset, Handler, CustodyEvent

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_uid', 'name', 'created_at')

@admin.register(Handler)
class HandlerAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_at')

@admin.register(CustodyEvent)
class CustodyEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset', 'handler', 'timestamp', 'is_anchored')
