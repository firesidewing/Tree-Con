from rest_framework import serializers

from .models import LatLong, Location, PlotData, Plot


class LatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLong
        fields = ('url', 'location_key', 'lat', 'long',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'block', 'license', 'cutting_permit',)


class PlotDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotData
        fields = ('id', 'plot_key', 'tree', 'species', 'dbh', 'height', 'gross_piece_size', 'net_piece_size',)


class PlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plot
        fields = ('id', 'userkey', 'plot_number', 'location')
        read_only_fields = ('userkey',)
