from django.shortcuts import render, redirect, get_object_or_404
from .models import Temperature
from rest_framework import viewsets
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import TemperatureSerializer 
from django.contrib.auth import login, authenticate, logout
from rest_framework.permissions import IsAuthenticated



# Create your views here.

def home(request):
  if request.user.is_authenticated:
    return render(request, "index.html", {})
  else:    
   return redirect(userLogin)

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
  
def logOut(request):
  logout(request)
  return render(request, "login.html", {})

def blank(request):
	return render(request, "blank.html", {})

def temperatureList(request): 
    #Delete
    if request.POST: 
      if request.POST['action'] == "delete":  
        tempId = request.POST['temp_id'] 
        temperature = Temperature.objects.get(pk=tempId)   
        temperature.delete()
        return redirect(temperatureList)
    else:
      temperature = Temperature.objects.all()    
      temperatures = {'temperatures': temperature}     
      return render(request,"temp-table.html", temperatures)   
    
  
def temperatureCreate(request): 
  if request.POST: 
    newTemperature = Temperature()
    newTemperature.value = request.POST['value']
    newTemperature.save()
    return redirect(temperatureList)
  else:
    return render(request, "temp-add.html")    
  
def temperatureListOne(request, id):  
    temperature = Temperature.objects.get(id=id)   
    temperatures = {'temperatures': temperature}     
    return render(request,"temp-single.html", temperatures)  
  
def temperatureUpdate(request, id): 
  temperature = Temperature.objects.get(id=id)   
  temperatures = {'temperatures': temperature}   
  if request.POST: 
    tempId = request.POST['temp_id'] 
    updatedTemperature = Temperature.objects.get(pk=tempId) 
    updatedTemperature.value = request.POST['value']
    updatedTemperature.save()    
    return redirect(temperatureList)
  else:
    return render(request, "temp-update.html", temperatures)  
  
def temperatureGraphs(request):
  temperature = Temperature.objects.all()    
  temperatures = {'temperatures': temperature}  
  return render(request, "temp-graphs.html", temperatures)
  
#Rest Api
class TemperatureViewset(viewsets.ViewSet):
  permission_classes = (IsAuthenticated,)  
  def create(self, request):
    serializer = TemperatureSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)            
    the_response = TemperatureSerializer(serializer.save())
    return Response(the_response.data, status=status.HTTP_201_CREATED)
     
  

