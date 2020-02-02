from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_tracking.mixins import LoggingMixin
from . import permissions
from .models import LatLong, Location, PlotData, Plot
from .serializers import LatLongSerializer, LocationSerializer, PlotDataSerializer, PlotSerializer


class LatLongViewSet(viewsets.ModelViewSet):
    queryset = LatLong.objects.all()
    serializer_class = LatLongSerializer
    permission_classes = (permissions.LatLong,)
    filter_backends = [DjangoFilterBackend]


class LocationViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.Location,)


class PlotDataViewSet(viewsets.ModelViewSet):
    queryset = PlotData.objects.all()
    serializer_class = PlotDataSerializer
    permission_classes = (permissions.PlotData,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plot_key']


class PlotViewSet(viewsets.ModelViewSet):    
    serializer_class = PlotSerializer
    permission_classes = (permissions.Plots,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location']

    def get_queryset(self):
        user = self.request.user.id
        return Plot.objects.filter(userkey_id=user)

    def perform_create(self, serializer):
        serializer.save(userkey=self.request.user)

