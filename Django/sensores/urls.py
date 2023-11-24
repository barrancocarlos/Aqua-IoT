from django.urls import path, include
from sensores import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('temperatura-aquario', views.TemperaturaAquarioViewset, basename='temperatura-aquario')
router.register('umidade', views.UmidadeViewset, basename='umidade')
router.register('nivel', views.NivelAguaViewset, basename='nivel')
router.register('temperatura-plantas', views.TemperaturaPlantasViewset, basename='temperatura-plantas')

urlpatterns = [    
    path('', views.home, name='home'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.logOut, name='logout'),    
    path('temp-aquario/', views.temperaturaAquario, name='temp-aquario'),
    path('temp-plantas/', views.temperaturaPlantas, name='temp-plantas'),
    path('umidade/', views.umidade, name='umidade'),
    path('nivel/', views.nivelAgua, name='nivel'),
    path('ldr/', views.ldr, name='ldr'),
    path('tds/', views.tds, name='tds'),
    path('api/', include(router.urls)),         
]