from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from . import permissions
from .models import LatLong, Location, PlotData, Plot, Species
from .serializers import (
    LatLongSerializer,
    LocationSerializer,
    PlotDataSerializer,
    PlotSerializer,
    SpeciesSerializer,
)


class LatLongViewSet(viewsets.ModelViewSet):
    queryset = LatLong.objects.all()
    serializer_class = LatLongSerializer
    permission_classes = (permissions.LatLong,)
    filter_backends = [DjangoFilterBackend]


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.Location,)


class PlotDataViewSet(viewsets.ModelViewSet):
    queryset = PlotData.objects.prefetch_related()
    serializer_class = PlotDataSerializer
    permission_classes = (permissions.PlotData,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["plot_key"]


class PlotViewSet(viewsets.ModelViewSet):
    serializer_class = PlotSerializer
    permission_classes = (permissions.Plots,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["location"]

    def get_queryset(self):
        user = self.request.user.id
        return Plot.objects.filter(userkey_id=user).prefetch_related()

    def perform_create(self, serializer):
        serializer.save(userkey=self.request.user)


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    permission_classes = (permissions.Species,)
