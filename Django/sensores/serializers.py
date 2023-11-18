from rest_framework import serializers
from .models import Temperature

class TemperatureSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Temperature
        fields = '__all__'
        depth = 1

    def create(self, validated_data):        
        temperature = Temperature.objects.create(**validated_data)        
        temperature.save()
        return temperature