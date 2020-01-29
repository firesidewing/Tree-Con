from rest_framework import viewsets

from . import permissions
from .models import LatLong, Location, PlotData, Plot
from .serializers import LatLongSerializer, LocationSerializer, PlotDataSerializer, PlotSerializer


class LatLongViewSet(viewsets.ModelViewSet):
    queryset = LatLong.objects.all()
    serializer_class = LatLongSerializer
    permission_classes = (permissions.LatLong,)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.Location,)


class PlotDataViewSet(viewsets.ModelViewSet):
    queryset = PlotData.objects.all()
    serializer_class = PlotDataSerializer
    permission_classes = (permissions.PlotData,)


class PlotViewSet(viewsets.ModelViewSet):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permission_classes = (permissions.Plots,)

    def perform_create(self, serializer):
        serializer.save(userkey=self.request.user)

