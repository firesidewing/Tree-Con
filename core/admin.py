from django.contrib import admin

from .models import LatLong, Location, PlotData, Plot, Species


class LatLongAdmin(admin.ModelAdmin):
    model = LatLong
    list_display = ["location_key"]
    search_fields = ["location_key"]
    list_select_related = True


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ["name", "block", "license", "cutting_permit", "baf"]
    search_fields = ["name", "block", "license", "cutting_permit"]


class PlotDataAdmin(admin.ModelAdmin):
    model = PlotData
    list_display = ["plot_key", "tree_species", "blowdown"]
    search_fields = ["plot_key"]
    list_select_related = True


class PlotAdmin(admin.ModelAdmin):
    model = Plot
    list_display = [
        "userkey",
        "plot_number",
        "location",
        "slope",
        "gross_volume_ha",
        "net_volume_ha",
        "timber_type",
    ]
    search_fields = ["userkey", "location"]
    list_select_related = True


class SpeciesAdmin(admin.ModelAdmin):
    model = Species
    list_display = [
        "id",
        "species_name",
        "fiz",
        "loss_factor",
        "vol_type",
        "vol_const_a",
        "vol_const_b",
        "vol_const_c",
    ]
    search_fields = ["species_name", "fiz", "vol_type"]


admin.site.register(LatLong, LatLongAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(PlotData, PlotDataAdmin)
admin.site.register(Plot, PlotAdmin)
admin.site.register(Species, SpeciesAdmin)
