from rest_framework import serializers

from .models import LatLong, Location, PlotData, Plot, Species


class LatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLong
        fields = (
            "url",
            "location_key",
            "lat",
            "long",
        )


class LocationSerializer(serializers.ModelSerializer):
    bec_zone = serializers.CharField(source="bec.short", read_only=True)

    class Meta:
        model = Location
        fields = ("id", "bec_zone", "name", "block", "license", "cutting_permit", "baf")


class PlotDataSerializer(serializers.ModelSerializer):
    tree_name = serializers.CharField(
        source="tree_species.species_name", read_only=True
    )

    class Meta:
        model = PlotData
        fields = (
            "id",
            "plot_key",
            "tree",
            "tree_species",
            "tree_name",
            "dbh",
            "height",
            "gross_piece_size",
            "net_piece_size",
            "blowdown",
            "alive",
        )

    def create(self, validated_data):
        d = {
            "plot_key_id": validated_data.get("plot_key", None).id,
            "tree": validated_data.get("tree", None),
            "tree_species": validated_data.get("tree_species", None).id,
            "dbh": validated_data.get("dbh", None),
            "height": validated_data.get("height", None),
            "gross_piece_size": validated_data.get("gross_piece_size", None),
            "net_piece_size": validated_data.get("net_piece_size", None),
            "blowdown": validated_data.get("blowdown", None),
            "alive": validated_data.get("alive", None),
        }
        plot_data, created = PlotData.objects.update_or_create(
            plot_key_id=d["plot_key_id"], tree=d["tree"], defaults=d,
        )
        return plot_data


class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = (
            "id",
            "userkey",
            "plot_number",
            "location",
            "slope",
            "gross_volume_ha",
            "net_volume_ha",
            "timber_type",
        )
        read_only_fields = ("userkey",)

    def create(self, validated_data):
        d = {
            "plot_number": validated_data.get("plot_number", None),
            "location_id": validated_data.get("location", None).id,
            "userkey_id": validated_data.get("userkey", None).id,
            "slope": validated_data.get("slope", None),
            "gross_volume_ha": validated_data.get("gross_volume_ha", None),
            "net_volume_ha": validated_data.get("net_volume_ha", None),
            "timber_type": validated_data.get("timber_type", None),
        }
        plot, created = Plot.objects.update_or_create(
            location_id=d["location_id"],
            plot_number=d["plot_number"],
            userkey_id=d["userkey_id"],
            defaults=d,
        )
        return plot


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = (
            "id",
            "species_name",
            "loss_factor",
            "bec",
            "vol_type",
            "vol_const_a",
            "vol_const_b",
            "vol_const_c",
        )
