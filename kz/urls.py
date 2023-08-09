from django.urls import path
from .views import EventsViewSet


urlpatterns = [
    path('events/', EventsViewSet.as_view(), name="events-all")
]
