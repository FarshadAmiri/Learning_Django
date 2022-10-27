from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import *
from users.api.permissions import IsAdmin
from flights.models import Flight
from rest_framework.permissions import IsAdminUser

# class SearchFlightAPI(GenericAPIView):
#     permission_classes = (IsAuthenticated, IsAdmin)


class ReadUpdateFlightAPI_GenericAPIView(GenericAPIView):
    permission_classes = [IsAdmin,]
    serializer_class = FlightSerializer
    def get(self, request, flight_id):
        flight = get_object_or_404(Flight, id=flight_id)
        data = self.get_serializer(flight).data  #Also try without ".data"
        return Response(data={'flight': data})

    def put(self, request, flight_id):
        flight = get_object_or_404(Flight, id=flight_id)
        flight_serialized = FlightSerializer(
            instance=flight,
            data= request.data,
            partial=True)
        if flight_serialized.is_valid():
            print("it's valid")
            flight_serialized.save()
            return Response({'message': 'Flight Updated Successfully'})
        return Response({'message': flight_serialized.errors})


class CreateFlightAPI_GenericAPIView(GenericAPIView):
    permission_classes = [IsAdmin,]
    serializer_class = FlightSerializer

    def post(self, request):
        flight_serialized = FlightSerializer(data=request.data)
        if flight_serialized.is_valid():
            flight_serialized.save()
            return Response(data={'message': 'Flight Added Successfully'})
        return Response(data={'message': flight_serialized.errors})


class ReadUpdateDeleteFlightAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser,]
    serializer_class = FlightSerializer
    lookup_url_kwarg = 'flight_id'
    queryset = Flight.objects.all()


class CreateListFlightAPI(ListCreateAPIView):
    permission_classes = [IsAdminUser,]
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()