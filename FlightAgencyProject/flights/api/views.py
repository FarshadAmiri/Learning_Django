from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import *
from users.api.permissions import IsAdmin
from flights.models import Flight


# class SearchFlightAPI(GenericAPIView):
#     permission_classes = (IsAuthenticated, IsAdmin)


class ReadUpdateFlightAPI(GenericAPIView):
    permission_classes = (IsAdmin)
    serializer_class = FlightSerializer
    def get(self, request, flight_id):
        flight = Flight.objects.get(id=flight_id)
        data = self.get_serializer(flight).data   #Also try without ".data"
        return Response(data={'flight': data})

    def put(self, request, flight_id):
        flight = Flight.objects.get(id= flight_id)
        flight_serialized = FlightSerializer(
            instance=flight,
            data= request.data,
            partial=True)
        if flight_serialized.is_valid():
            flight_serialized.save()
            return Response(data={'message': 'Flight Updated Successfully'})
        return Response(data={'message': flight_serialized.errors})


class AddFlightAPI(GenericAPIView):
    permission_classes = (IsAdmin)
    serializer_class = FlightSerializer

    def post(self, request):
        flight_serialized = FlightSerializer(request.data)
        if flight_serialized.is_valid():
            flight_serialized.save()
            return Response(data={'message': 'Flight Added Successfully'})
        return Response(data={'message': flight_serialized.errors})