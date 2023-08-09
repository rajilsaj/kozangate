from rest_framework import serializers
from .models import Events


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("title", "description", "startDate", "endDate", "allDay")
