from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'


class Airline(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Airport(models.Model):
    name = models.CharField(max_length=60)
    symbol = models.CharField(max_length=3)
    city = models.ForeignKey(City, related_name='airports' ,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city} ({self.symbol})'


class Flight(models.Model):
    origin = models.ForeignKey(Airport, related_name='flights_from', on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name='flights_to', on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return f'Flight{self.id} {self.origin.city}({self.origin.symbol}) to {self.destination.city}({self.destination.symbol}) via {self.airline}    {self.datetime.strftime("%d/%m/%y  %H:%M")}'

    def str2(self):
        return f'{self.origin.city} ({self.origin.symbol}) to {self.destination.city} ({self.destination.symbol})'


class Passenger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    national_id = models.CharField(max_length=12, verbose_name='National id', primary_key=True)
    # tickets = models.ManyToManyField(Flight)
    tickets = models.ManyToManyField(Flight)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


