from django.urls import path
from .views import CustodyEventListCreateView, AssetDetailView, ReceiveScanView

urlpatterns = [
    path('events/', CustodyEventListCreateView.as_view(), name='event-list'),
    path('scan/', ReceiveScanView.as_view(), name='receive-scan'),
    path('assets/<str:asset_uid>/', AssetDetailView.as_view(), name='asset-detail'),
]
