################# IMPORTS #####################################
from django.shortcuts import render,redirect
from login.funciones_auxiliares import *
###############################################################

#############################################
#Nombre Funcion: Login
#Tipo: Vista
#Funcionamiento: Vista de login del proyecto
#Output: Retorna la vista login
#############################################
def login(request):
    context={}
    if request.method =='POST':#Verificamos si se estan enviando datos
        if check_user(request)==0 and loguear_user(request)==0:#cheamos que el usuario existe y que fue exitosamente logueado
            return redirect("/user/")#redirgimos a la vista usuario
        else:
            context['error']="error"#Retornamos error
    return render(request,"login/login.html",context)#retornamos vista
