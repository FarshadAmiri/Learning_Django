from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from .models import Flight
from .forms import *


def homepage(request):
    if request.method == 'GET':
        form = SearchFlight()
        return render(request, "Homepage.html", context={'flights': Flight.objects.all(),'form': form
                                                         ,'user':request.user
                      })
    elif request.method == 'POST':
        form = SearchFlight(request.POST)
        if form.is_valid():
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            return HttpResponseRedirect(reverse('flights:search_flight', kwargs={'origin':origin, 'destination':destination}))
        return render(request, 'Error_page.html', {'message':form.errors['err']})


def search_flight(request, origin, destination):
    filtered_flights = Flight.objects.filter(origin__city__name=origin, destination__city__name=destination)
    return render(request, 'Search_Flight_Result.html', context={'origin': origin, 'destination': destination, 'filtered_flights': filtered_flights})


# @login_required(login_url='users:login')
# @permission_required('flights.add_passenger', login_url='users:login',)
def flight_detail_view(request, pk):
    flight = Flight.objects.get(pk=pk)
    if request.method == 'GET':
        passengers = flight.passenger_set.all()
        form = AddPassengerForm()
        return render(request, 'Flight_detail_Page.html', context={
            'flight':flight, 'passengers':passengers, 'form':form, 'pk':pk, 'user':request.user})
    elif request.method == 'POST':
        if not request.user.has_perm('flights.add_passenger'):
            raise PermissionDenied()
        form = AddPassengerForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.tickets.add(Flight.objects.get(pk=pk))
            p.save()
            form.save_m2m()
            passengers = Flight.objects.get(pk=pk).passenger_set.all()
            return render(request, 'Flight_detail_Page.html', context={
                'flight': flight, 'passengers': passengers, 'form': form, 'pk': pk,
                'message': 'Successfully booked'})
        elif (Passenger.objects.filter(national_id=form.data['national_id']).count() == 1):
            p = Passenger.objects.get(national_id=form.data['national_id'])
            if ((form.data['first_name'] == p.first_name) and (form.data['last_name'] == p.last_name)):
                if p not in Flight.objects.get(pk=pk).passenger_set.all():
                    p.tickets.add(Flight.objects.get(pk=pk))
                    p.save()
                    status = 'Successful'
                    msg = 'Successfully booked'

                else:
                    status = 'Unsuccessful'
                    msg = 'He/She is already booked on the flight'

            elif p not in Flight.objects.get(pk=pk).passenger_set.all():
                msg = 'A person with same national id number is registered on our database, but your enetered name is not corresponding to him/her! please check your entered data or contact us via phone or email'
                status = 'Unsuccessful'
            elif p in Flight.objects.get(pk=pk).passenger_set.all():
                msg = 'A person with same national id number is booked on this flight. However, your enetered name is not corresponding to him/her! Please check your entered data or contact us via phone or email'
                status = 'Unsuccessful'
        else:
            msg = form.errors

        passengers = Flight.objects.get(pk=pk).passenger_set.all()
        return render(request, 'Flight_detail_Page.html', context={
            'flight': flight, 'passengers': passengers, 'form': form, 'pk': pk,
            'message': msg})