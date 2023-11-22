from django.db import models

# Create your models here.

class Sensor(models.Model):
  nome = models.CharField(max_length=50)
  tipo = models.CharField(max_length=50)
  grupo = models.CharField(max_length=50)
  unidade_medida = models.CharField(max_length=50)  
  data_criacao = models.DateTimeField(auto_now_add=True)
  class Meta:
    abstract = True
    
class TemperaturaPlantas(Sensor):
  temperatura = models.FloatField(max_length=200, default='00')
  unidade_medida = models.CharField(max_length=50, default='Graus')  
  
class Umidade(Sensor):
  umidade = models.FloatField(max_length=200, default='00')
  unidade_medida = models.CharField(max_length=50, default='Porcentagem')
  
class TemperaturaAquario(Sensor):
  temperatura = models.FloatField(max_length=200, default='00')
  unidade_medida = models.CharField(max_length=50, default='Graus')    
  
class NivelAgua(Sensor):
  nivel = models.FloatField(max_length=200, default='00')
  nivel_minimo = models.FloatField(max_length=200, default='30')
  unidade_medida = models.CharField(max_length=50, default='Centímetros')
  
class Ldr(Sensor):
  luminosidade = models.FloatField(max_length=200, default='00')
  media_luminosidade = models.FloatField(max_length=200, default='30')
  unidade_medida = models.CharField(max_length=50, default='Lux') 
  
class Tds(Sensor):
  tds = models.FloatField(max_length=200, default='00')
  media_tds = models.FloatField(max_length=200, default='30')
  unidade_medida = models.CharField(max_length=50, default='Ppm')    
  


class Temperature(models.Model):
  value = models.FloatField(max_length=200, default='00')
  creation_date = models.DateTimeField(auto_now_add=True)
  
  
  
  def __str__(self):
        return str(self.value)
