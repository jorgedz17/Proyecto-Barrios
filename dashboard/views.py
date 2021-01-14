#!/usr/bin/env python
# -*- coding: utf-8 -*-

################# IMPORTS #####################################
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
import json
from dashboard.models import *
###############################################################



#############################################
#Nombre Funcion: Index
#Tipo: Vista
#Funcionamiento: Vista principal del proyecto
#Output: Retorna la vista principal
#############################################
def index(request):
    context = {'is_staff':request.user.is_staff,#Pasamos el valor si es staff
            'username': request.user.username,# Pasamos el nombre de Usuario
            'tdata': '/data/', #La dirección a donde estan los datos de las zonas
            'tmarkers': '/markers/',# La dirección de los market
            'sdata': '/sdata/'} #La dirección de la data sensible
    return render(request,"index.html",context)

#############################################
#Nombre Funcion: About
#Tipo: Vista
#Funcionamiento: Vista sobre nosotros
#Output: Retorna la vista about
#############################################
def about(request):
    return render(request,"about.html")

#############################################
#Nombre Funcion: territorial data
#Tipo: Vista-Rest
#Funcionamiento: Retorna un json con la data de las zonas
#Output: Retorna el json en httpresponse
#############################################
def territorial_data(request):
    region = request.POST.get('region', 'Valparaiso')
    with open('RiskmapApp/data/data_UV17_valpo_010420.json', 'r') as fin:#Abrimos el archivo
        data = json.load(fin)#cargamos
    return HttpResponse(json.dumps(data), content_type="application/json")#Retorna el serializado del archivo de las zonas 

#############################################
#Nombre Funcion: Markers Data
#Tipo: Vista-Rest
#Funcionamiento: Retorna Json de los markest de la BD
#Output:  Retorna el json en httpresponse
#############################################
def markers_data(request):    
    puntos=Puntos.objects.all()#obtenemos todos los puntos
    post_list = serializers.serialize('json', puntos)#serializamos 
    return HttpResponse(post_list, content_type="application/json")#Retornamos


#############################################
#Nombre Funcion: Cargar puntos BD
#Tipo: Vista auxiliar
#Funcionamiento: vista solamente carga los puntos existentes en el archivo markers_data.json a la bd
# ocupar con cuidado ya que podria causar duplicados.
#Output: Retorna json en httpresponse
#############################################
#def cargar_puntos_bd(request):
#    with open('dashboard/data/markers_data.json', encoding='utf-8') as fh: #abrimos el archivo
#        data = json.load(fh) 
#    for i in data:#por cada market presente en el archivo
#        punto_aux=Puntos()#creamos el punto y cargamos datos
#        punto_aux.nombre=i["name"]
#        punto_aux.lat=i["lat"]
#        punto_aux.lng=i["lng"]
#        tipo_aux=Tipos.objects.get(nombre=i["tipo"])#buscamos el tipo de punto
#        punto_aux.tipo=tipo_aux
#        punto_aux.save()
#    return HttpResponse(json.dumps(data), content_type="application/json")