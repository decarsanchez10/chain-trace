from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Asset, Handler, CustodyEvent
from .serializers import AssetSerializer, HandlerSerializer, CustodyEventSerializer

class CustodyEventListCreateView(generics.ListCreateAPIView):
    queryset = CustodyEvent.objects.all().order_by('-timestamp')
    serializer_class = CustodyEventSerializer

class AssetDetailView(generics.RetrieveAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    lookup_field = 'asset_uid'

class ReceiveScanView(APIView):
    def post(self, request):
        serializer = CustodyEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
