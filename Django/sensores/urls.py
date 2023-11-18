from django.urls import path, include
from django.views.generic import TemplateView
from sensores import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('temperatures', views.TemperatureViewset, basename='temperatures')

urlpatterns = [    
    path('', views.home, name='home'),
    path('blank-page/', views.blank, name='blank'), 
    path('login/', views.userLogin, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('temp-table/', views.temperatureList, name='temp-table'),
    path('temp-add/', views.temperatureCreate, name='temp-add'),
    path('temp-update/<int:id>/', views.temperatureUpdate, name='temp-update'),    
    path('temp-single/<int:id>/', views.temperatureListOne, name='temp-single'),
    path('temp-graphs/', views.temperatureGraphs, name='temp-graphs'),
    path('api/', include(router.urls)),         
]