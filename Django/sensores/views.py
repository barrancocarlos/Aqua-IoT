from django.shortcuts import render, redirect, get_object_or_404
from .models import TemperaturaPlantas, Umidade, TemperaturaAquario, NivelAgua, Ldr, Tds
from rest_framework import viewsets
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import TemperaturaAquarioSerializer, UmidadeSerializer, NivelAguaSerializer, TemperaturaPlantasSerializer, LdrSerializer
from django.contrib.auth import login, authenticate, logout
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Dashboard
def home(request):
  if request.user.is_authenticated:
    # Temperatura Plantas
    temperaturap = TemperaturaPlantas.objects.all()  
    # Nivel Agua 
    nivel = NivelAgua.objects.all()   
    # Umidade
    umidade = Umidade.objects.all() 
    # TDS
    tds = Tds.objects.all()  
    # Temperatura Aquario 
    temperaturaa = TemperaturaAquario.objects.all() 
    # LDR
    ldr = Ldr.objects.all()  
    # Dados  
    context = {
              'temperaturas': temperaturap,
              'nivels': nivel,
              'umidades': umidade,
              'tdss': tds,
              'temperaturaas': temperaturaa,
              'ldrs': ldr,
       }
    return render(request, "index.html", context)
  else:    
   return redirect(userLogin)

# Login
def userLogin(request):
  if request.POST:
     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(username=username, password=password)
     if user is not None:
       if user.is_active:
         login(request, user)
         return redirect(home)
  else: 
    return render(request, "login.html", {})

# Logout  
def logOut(request):
  logout(request)
  return render(request, "login.html", {})

# Temperatura Aquario
def temperaturaAquario(request):
  temperatura = TemperaturaAquario.objects.all()    
  temperaturas = {'temperaturas': temperatura}  
  return render(request, "temp-aquario.html", temperaturas)

# Umidade
def umidade(request):
  umidade = Umidade.objects.all()    
  umidades = {'umidades': umidade}  
  return render(request, "umidade.html", umidades)

# Nivel Agua
def nivelAgua(request):
  nivel = NivelAgua.objects.all()    
  nivels = {'nivels': nivel}  
  return render(request, "nivel.html", nivels)

# Temperatura Plantas
def temperaturaPlantas(request):
  temperatura = TemperaturaPlantas.objects.all()    
  temperaturas = {'temperaturas': temperatura}  
  return render(request, "temp-plantas.html", temperaturas)

# LDR
def ldr(request):
  ldr = Ldr.objects.all()    
  ldrs = {'ldrs': ldr}  
  return render(request, "ldr.html", ldrs)

# TDS
def tds(request):
  tds = Tds.objects.all()    
  tdss = {'tdss': tds}  
  return render(request, "tds.html", tdss) 
  
#Rest Api

# Temperatura Aquario
class TemperaturaAquarioViewset(viewsets.ViewSet):
  permission_classes = (IsAuthenticated,)  
  def create(self, request):
    serializer = TemperaturaAquarioSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)            
    the_response = TemperaturaAquarioSerializer(serializer.save())
    return Response(the_response.data, status=status.HTTP_201_CREATED)
  
# Umidade
class UmidadeViewset(viewsets.ViewSet):
  permission_classes = (IsAuthenticated,)  
  def create(self, request):
    serializer = UmidadeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)            
    the_response = UmidadeSerializer(serializer.save())
    return Response(the_response.data, status=status.HTTP_201_CREATED)
  
# Nivel Agua
class NivelAguaViewset(viewsets.ViewSet):
  permission_classes = (IsAuthenticated,)  
  def create(self, request):
    serializer = NivelAguaSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)            
    the_response = NivelAguaSerializer(serializer.save())
    return Response(the_response.data, status=status.HTTP_201_CREATED)

# Temperatura Plantas
class TemperaturaPlantasViewset(viewsets.ViewSet):
  permission_classes = (IsAuthenticated,)  
  def create(self, request):
    serializer = TemperaturaPlantasSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)            
    the_response = TemperaturaPlantasSerializer(serializer.save())
    return Response(the_response.data, status=status.HTTP_201_CREATED)
  
# LDR
class LdrViewset(viewsets.ViewSet):
  permission_classes = (IsAuthenticated,)  
  def create(self, request):
    serializer = LdrSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)            
    the_response = LdrSerializer(serializer.save())
    return Response(the_response.data, status=status.HTTP_201_CREATED)
   
     
  

