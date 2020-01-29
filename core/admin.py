from django.contrib import admin

from .models import LatLong, Location, PlotData, Plot


class LatLongAdmin(admin.ModelAdmin):
    model = LatLong
    list_display = ['location_key']
    search_fields = ['location_key']
    list_select_related = True


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ['name', 'block', 'license', 'cutting_permit']
    search_fields = ['name', 'block', 'license', 'cutting_permit']


class PlotDataAdmin(admin.ModelAdmin):
    model = PlotData
    list_display = ['plot_key']
    search_fields = ['plot_key']
    list_select_related = True


class PlotAdmin(admin.ModelAdmin):
    model = Plot
    list_display = ['userkey', 'plot_number', 'location']
    search_fields = ['userkey', 'location']
    list_select_related = True


admin.site.register(LatLong, LatLongAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(PlotData, PlotDataAdmin)
admin.site.register(Plot, PlotAdmin)