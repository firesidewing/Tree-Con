from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from core.views import LatLongViewSet, LocationViewSet, PlotDataViewSet, PlotViewSet

router = routers.DefaultRouter()
router.register(r'core/lat-longs', LatLongViewSet)
router.register(r'core/locations', LocationViewSet)
router.register(r'core/plot-datas', PlotDataViewSet)
router.register(r'core/plot', PlotViewSet)

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('treecon/', admin.site.urls),
    path('api/docs/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/', include(router.urls))
]
