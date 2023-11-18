from django.db import models

# Create your models here.

class Temperature(models.Model):
  value = models.FloatField(max_length=200, default='00')
  creation_date = models.DateTimeField(auto_now_add=True)
  
  
  
  def __str__(self):
        return str(self.value)
