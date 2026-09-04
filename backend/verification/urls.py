from django.urls import path
from .views import VerifyEventView, VerifyAssetChainView

urlpatterns = [
    path('event/<int:event_id>/', VerifyEventView.as_view(), name='verify-event'),
    path('asset/<str:asset_uid>/', VerifyAssetChainView.as_view(), name='verify-asset-chain'),
]

