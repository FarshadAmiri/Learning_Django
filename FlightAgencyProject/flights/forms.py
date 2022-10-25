from django import forms
from django.forms import ModelForm
from .models import *


class SearchFlight(forms.Form):
    CITIES = City.objects.only('name')
    origin = forms.ModelChoiceField(queryset=CITIES)
    destination = forms.ModelChoiceField(queryset=CITIES)

    def clean_destination(self):
        destination = self.cleaned_data['destination']
        origin = self.cleaned_data['origin']
        if (destination != origin):
            return destination
        else:
            message = 'Origin and Destination cannot be the same'
            self.errors['err'] = message


class AddPassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'national_id']

    def save(self, commit=True):
        data = super(AddPassengerForm, self).save(commit=commit)
        if Passenger.objects.filter(national_id = self.cleaned_data['national_id']).count() == 0:
            # p = Passenger.objects.create(first_name=self.data['first_name'], last_name=self.data['last_name'],
            #                          national_id=self.data['national_id'])
            p = Passenger.objects.create(first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'],
                                     national_id=self.cleaned_data['national_id'])
        else:
            p = Passenger.objects.get(national_id=self.cleaned_data['national_id'])
        p.save()
        return p


