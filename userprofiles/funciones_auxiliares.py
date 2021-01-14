################# IMPORTS #####################################
from dashboard.models import *
from django.contrib import auth
###############################################################

#############################################
#Nombre Funcion: Buscar Tipos
#Tipo: Funcion Auxiliar
#Funcionamiento: busca los tipos de puntos
#Output: Retorna los tipos de puntos
#############################################
def buscar_tipos(request,context):
    tipos = Tipos.objects.all()#busca todos los tipos de puntos
    context["tipos"] = tipos
    return context#devolvemos


#############################################
#Nombre Funcion: check login user
#Tipo: Funcion Auxiliar
#Funcionamiento: chequeamos usuario logueado
#Output: Retorna usuario logueado
#############################################
def check_login_user(request,context):
    if request.user.is_authenticated:
        context["logueado"]="si"
    return context

#############################################
#Nombre Funcion: agregar punto aux
#Tipo: Funcion Auxiliar
#Funcionamiento: crea un punto con los datos recibidos
#Output: retorna exito o exito
#############################################
def agregar_punto_aux(request,context):
    #Verificamos que esten todos los datos de entrada
    if ("nombre" in request.POST.keys()) and ("tipo" in request.POST.keys()) and ("lat" in request.POST.keys()) and ("lng" in request.POST.keys()):
        aux_punto=Puntos()
        #Le asignamos los puntos al punto
        aux_punto.nombre=request.POST["nombre"]
        aux_punto.lat=request.POST["lat"]
        aux_punto.lng=request.POST["lng"]
        tipo=Tipos.objects.filter(nombre=request.POST["tipo"])
        aux_punto.tipo=tipo[0]#Asignamos el tipo de punto
        aux_punto.save()
        context["exito"]="exito"
        return context
    else:
        context["error"]="error"
        return context

#############################################
#Nombre Funcion: actualizar punto aux
#Tipo: Funcion Auxiliar
#Funcionamiento: actualiza un punto con los datos recibidos
#Output: retorna exito o exito
#############################################
def actualizar_punto_aux(request,context):
    if ("nombre" in request.POST.keys()) and ("tipo" in request.POST.keys()) and ("pk" in request.POST.keys()):
        aux_punto=Puntos.objects.get(id=request.POST["pk"])#Vamos a buscar el punto por la pk
        aux_punto.nombre=request.POST["nombre"]#actualizamos el nombre
        tipo=Tipos.objects.filter(nombre=request.POST["tipo"])#actualizamos el tipo 
        aux_punto.tipo=tipo[0]
        aux_punto.save()
        context["actualizacion"]="exito"
        return context
    else:
        context["error"]="error"
        return context


#############################################
#Nombre Funcion: eliminar punto aux
#Tipo: Funcion Auxiliar
#Funcionamiento: eliminar un punto con los datos recibidos
#Output: retorna exito o exito
#############################################
def eliminar_punto_aux(request,context):
    if ("pk" in request.POST.keys()):#verificamos que exista pk
        aux_punto=Puntos.objects.get(id=request.POST["pk"])#vamos a buscar por la pk
        aux_punto.delete()#eliminamos
        context["eliminado"]="exito"
        return context
    else:
        context["error"]="error"
        return context
