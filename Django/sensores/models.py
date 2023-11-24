from django.db import models

# Create your models here.

class Sensor(models.Model):
  nome = models.CharField(max_length=50)
  tipo = models.CharField(max_length=50)
  grupo = models.CharField(max_length=50)  
  data_criacao = models.DateTimeField(auto_now_add=True)
  class Meta:
    abstract = True
    
class TemperaturaPlantas(Sensor):
  temperatura = models.FloatField(max_length=200, default='00')
  unidade_medida = models.CharField(max_length=50, default='Graus') 
  def __str__(self):
        return str(self.temperatura) + str(self.unidade_medida)  
  
class Umidade(Sensor):
  umidade = models.FloatField(max_length=200, default='00')
  unidade_medida = models.CharField(max_length=50, default='Porcentagem')
  def __str__(self):
        return str(self.umidade) + str(self.unidade_medida)
  
class TemperaturaAquario(Sensor):
  temperatura = models.FloatField(max_length=200, default='00')
  unidade_medida = models.CharField(max_length=50, default='Graus') 
  def __str__(self):
        return str(self.temperatura) + str(self.unidade_medida)  
  
class NivelAgua(Sensor):
  nivel = models.FloatField(max_length=200, default='00')
  nivel_minimo = models.FloatField(max_length=200, default='30')
  unidade_medida = models.CharField(max_length=50, default='Centímetros')
  def __str__(self):
        return str(self.nivel) + str(self.unidade_medida)
  
class Ldr(Sensor):
  luminosidade = models.FloatField(max_length=200, default='00')
  media_luminosidade = models.FloatField(max_length=200, default='30')
  unidade_medida = models.CharField(max_length=50, default='Lux') 
  def __str__(self):
        return str(self.luminosidade) + str(self.unidade_medida)
  
class Tds(Sensor):
  tds = models.FloatField(max_length=200, default='00')
  media_tds = models.FloatField(max_length=200, default='30')
  unidade_medida = models.CharField(max_length=50, default='Ppm')
  def __str__(self):
        return str(self.tds) + str(self.unidade_medida)   