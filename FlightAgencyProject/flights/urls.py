from django.urls import path
from .views import *
from .api.views import *

app_name = 'flights'
urlpatterns = [
    path('',homepage, name='homepage'),
    path('origin=<str:origin>&destination=<str:destination>', search_flight, name='search_flight'),
    path('flight?<int:pk>', flight_detail_view, name='flight_detail'),
    path('flight-api_GenericAPIView/<int:flight_id>/', ReadUpdateFlightAPI_GenericAPIView.as_view()), #X
    path('create-flight-api_GenericAPIView/', CreateFlightAPI_GenericAPIView.as_view()), #X
    path('readupdatedelete-flight-api/<int:flight_id>/', ReadUpdateDeleteFlightAPI.as_view()),
    path('create-list-flight-api/', CreateListFlightAPI.as_view())
]