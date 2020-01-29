from rest_framework import serializers

from .models import LatLong, Location, PlotData, Plot


class LatLongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LatLong
        fields = ('url', 'location_key', 'lat', 'long',)


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url', 'name', 'block', 'license', 'cutting_permit',)


class PlotDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlotData
        fields = ('url', 'plot_key', 'tree', 'species', 'dbh', 'height', 'gross_piece_size', 'net_piece_size',)


class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ('url', 'userkey', 'plot_number', 'location',)
        read_only_fields = ('userkey',)
