from .models import Events
from django.urls import reverse
from rest_framework import status
from .serializers import EventsSerializer
from datetime import datetime, timedelta, timezone
from rest_framework.test import APITestCase, APIClient


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_event(title="", description="", startDate="", endDate="", allDay=""):
        if title != "" and description != "" and startDate != "" and endDate != "":
            Events.objects.create(
                title=title, description=description, startDate=startDate, endDate=endDate, allDay=allDay)

    def setUp(self):
        # add test data
        self.create_event('Work Fair GOOGLE', ' This event is about people who plan to work for FAANG someday',
                          datetime.now(tz=timezone.utc),  datetime.now(tz=timezone.utc) + timedelta(hours=1),  True)
        self.create_event('Work Fair AMAZON', ' This event is about people who plan to work for FAANG someday',
                          datetime.now(tz=timezone.utc),  datetime.now(tz=timezone.utc) + timedelta(hours=1),  True)
        self.create_event('Work Fair IBM', ' This event is about people who plan to work for FAANG someday',
                          datetime.now(tz=timezone.utc),  datetime.now(tz=timezone.utc) + timedelta(hours=1),  True)
        self.create_event('Work Fair JUKA', ' This event is about people who plan to work for FAANG someday',
                          datetime.now(tz=timezone.utc),  datetime.now(tz=timezone.utc) + timedelta(hours=1),  True)


class GetAllEventsTest(BaseViewTest):

    def test_get_all_events(self):
        """
        This test ensures that all events added in the setUp method
        exist when we make a GET request to the events/ endpoint
       """
        # hit the API endpoint
        response = self.client.get(
            reverse("events-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Events.objects.all()
        serialized = EventsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
