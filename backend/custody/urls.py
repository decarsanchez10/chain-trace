from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustodyEventListCreateView, AssetDetailView, ReceiveScanView,
    AssetHistoryView, HandlerViewSet, AssetViewSet
)

router = DefaultRouter()
router.register(r'handlers', HandlerViewSet, basename='handler')
router.register(r'assets', AssetViewSet, basename='asset')

urlpatterns = [
    path('', include(router.urls)),
    path('events/', CustodyEventListCreateView.as_view(), name='event-list'),
    path('scan/', ReceiveScanView.as_view(), name='receive-scan'),
    path('assets/<str:asset_uid>/history/', AssetHistoryView.as_view(), name='asset-history'),
]

