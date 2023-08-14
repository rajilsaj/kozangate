from rest_framework import serializers
from .models import Events, Users, Calendars


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("title", "description", "startDate", "endDate", "allDay")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("name", "email", "phoneNumber")


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendars
        fields = ("name", "description", "timezone")
