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

    def create(self, validated_data):
        d = {
            'plot_number': validated_data.get('plot_number', None),
            'location_id': validated_data.get('location', None).id,
            'userkey_id': validated_data.get('userkey', None).id
        }
        plot, created = Plot.objects.update_or_create(
            location_id=d['location_id'],
            plot_number=d['plot_number'],
            userkey_id=d['userkey_id'],
            defaults=d)
        return plot
