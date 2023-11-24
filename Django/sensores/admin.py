from django.contrib import admin
from .models import TemperaturaPlantas, Umidade, TemperaturaAquario, NivelAgua, Ldr, Tds

# Register your models here.

admin.site.register(TemperaturaPlantas)
admin.site.register(Umidade)
admin.site.register(TemperaturaAquario)
admin.site.register(NivelAgua)
admin.site.register(Ldr)
admin.site.register(Tds)
