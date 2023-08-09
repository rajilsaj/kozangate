from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import EventsSerializer
from rest_framework import viewsets
from .models import Events


class EventsViewSet(viewsets.ViewSet):
    queryset = Events.objects.all()

    """
        A simple ViewSet for listing or retrieving events.

    """

    def list(self, request):
        serializer = EventsSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        serializer = EventsSerializer(event)
        return Response(serializer.data)
