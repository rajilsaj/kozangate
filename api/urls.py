from django.urls import path, re_path, include
from rest_framework import routers
from kz.views import EventsViewSet
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'events', EventsViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('api/(?P<version>(v1|v2))/', include('kz.urls')),
    path('api/', include(router.urls)),
]
