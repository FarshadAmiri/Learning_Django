from rest_framework import serializers
from ..models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class meta:
        model = Flight
        fields = '__all__'

    def validate(self, data):
        if data.get('origin',0) == data.get('destination',1):
            raise serializers.ValidationError('Origin and Destination cannot be same')
        return data

    def create(self, validated_data):
        flight = Flight.objects.create(**validated_data)
        return flight

    def update(self, instance ,validated_data):
        instance.origin = validated_data.get('origin', instance.origin)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.airline = validated_data.get('airline', instance.airline)
        instance.datetime = validated_data.get('datetime', instance.datetime)

        instance.save()
        return instance