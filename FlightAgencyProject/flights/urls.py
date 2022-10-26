from django.urls import path
from .views import *
from .api.views import *

app_name = 'flights'
urlpatterns = [
    path('',homepage, name='homepage'),
    path('origin=<str:origin>&destination=<str:destination>', search_flight, name='search_flight'),
    path('flight?<int:pk>', flight_detail_view, name='flight_detail'),
    path('flight-api&id=<int:flight_id>/', ReadUpdateFlightAPI.as_view()),
    path('add-flight-api/', AddFlightAPI.as_view()),
]