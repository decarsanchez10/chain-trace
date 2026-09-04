from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/custody/', include('custody.urls')),
    path('api/anchoring/', include('anchoring.urls')),
    path('api/verification/', include('verification.urls')),
]

