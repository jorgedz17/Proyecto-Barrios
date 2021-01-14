################# IMPORTS #####################################
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from userprofiles.funciones_auxiliares import  *
###############################################################


#############################################
#Nombre Funcion: index
#Tipo: Vista 
#Funcionamiento: Vista principal usuario
#Output: Retorna la vista principal usuario
#############################################
@login_required(login_url='/login')
def index(request):    
    context = check_login_user(request, {})#Sacamos datos del usuario
    context = buscar_tipos(request,context)#Sacamos datos de los tipos de puntos
    if request.method == "POST":#Verificamos si le estan enviando datos
        if request.POST["actualizacion"]=='0':#Verificamos si se esta agregando un punto
            context=agregar_punto_aux(request,context)
        elif request.POST["actualizacion"]=='1':#Verificamos si se esta actualizando un punto
            context=actualizar_punto_aux(request,context)
        else:#Verificamos si se esta eliminado un punto
            context=eliminar_punto_aux(request,context)
    return render(request,"userprofiles/index.html",context)

#############################################
#Nombre Funcion: logout_
#Tipo: Vista Auxiliar
#Funcionamiento: Esta vista es para cerrar sesión de un usuario
#Output: Retorna la vista login
#############################################
@login_required(login_url='/login')
def logout_(request):
	auth.logout(request)#cerramos la sesión
	return redirect("/login")# redirigimos al login
