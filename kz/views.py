from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import EventsSerializer
from rest_framework import viewsets
from .models import Events


class EventsViewSet(viewsets.ViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    """
        A simple ViewSet for listing or retrieving events.

    """

    def list(self, request):
        """
            List all events
        """
        return Response(self.serializer_class(self.queryset, many=True).data)

    def retrieve(self, request, pk=None):
        """
            Retrieve a single event by ID
        """
        event = get_object_or_404(self.queryset, pk=pk)
        serializer = EventsSerializer(event)
        return Response(serializer.data)
