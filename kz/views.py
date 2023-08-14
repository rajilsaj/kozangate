
from rest_framework.response import Response
from .serializers import EventsSerializer
from rest_framework import viewsets
from rest_framework import status
from .models import Events, Users


class EventsViewSet(viewsets.ViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    """
        A simple ViewSet for listing or retrieving events.

    """

    def list(self, request):
        """
            List all events.
        """
        return Response(self.serializer_class(self.queryset, many=True).data)

    def retrieve(self, request, pk=None):
        """
            Retrieve a single event by ID.
        """
        event = self.get_object(pk=pk)
        return Response(self.serializer_class(event).data)

    def create(self, request, pk=None):
        """
            Create a new event.
        """
        event_data = request.data.get('event')
        serializer = self.serializer_class(data=event_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
            Update an existing event.
        """
        event = self.get_object(pk=pk)
        event_data = request.data.get('event')
        serializer = self.serializer_class(instance=event, data=event_data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
            Delete an existing event.
        """
        event = self.get_object(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersViewSet(viewsets.ViewSet):
    pass
