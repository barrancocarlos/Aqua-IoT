from rest_framework import serializers
from .models import TemperaturaPlantas, Umidade, TemperaturaAquario, NivelAgua, Ldr, Tds

# Temperatura Aquario  
class TemperaturaAquarioSerializer(serializers.ModelSerializer):    
    class Meta:
        model = TemperaturaAquario
        fields = '__all__'
        depth = 1

    def create(self, validated_data):        
        temperatura = TemperaturaAquario.objects.create(**validated_data)        
        temperatura.save()
        return temperatura
    
# Umidade 
class UmidadeSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Umidade
        fields = '__all__'
        depth = 1

    def create(self, validated_data):        
        umidade = Umidade.objects.create(**validated_data)        
        umidade.save()
        return umidade
    
# Nivel Agua
class NivelAguaSerializer(serializers.ModelSerializer):    
    class Meta:
        model = NivelAgua
        fields = '__all__'
        depth = 1

    def create(self, validated_data):        
        nivel = NivelAgua.objects.create(**validated_data)        
        nivel.save()
        return nivel
    
# Temperatura Plantas
class TemperaturaPlantasSerializer(serializers.ModelSerializer):    
    class Meta:
        model = TemperaturaPlantas
        fields = '__all__'
        depth = 1

    def create(self, validated_data):        
        temperatura = TemperaturaPlantas.objects.create(**validated_data)        
        temperatura.save()
        return temperatura

# LDR
class LdrSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Ldr
        fields = '__all__'
        depth = 1

    def create(self, validated_data):        
        ldr = Ldr.objects.create(**validated_data)        
        ldr.save()
        return ldr

# TDS
class TdsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Tds
        fields = '__all__'
        depth = 1

    def create(self, validated_data):        
        tds = Tds.objects.create(**validated_data)        
        tds.save()
        return tds