from django.urls import path
from .views import VerifyEventView

urlpatterns = [
    path('verify/<int:event_id>/', VerifyEventView.as_view(), name='verify-event'),
]
