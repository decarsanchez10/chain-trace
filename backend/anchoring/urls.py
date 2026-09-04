from django.urls import path
from .views import AnchorTransactionListView, PendingAnchorView, TriggerAnchorView

urlpatterns = [
    path('transactions/', AnchorTransactionListView.as_view(), name='anchor-transactions'),
    path('pending/', PendingAnchorView.as_view(), name='anchor-pending'),
    path('trigger/', TriggerAnchorView.as_view(), name='anchor-trigger'),
]
