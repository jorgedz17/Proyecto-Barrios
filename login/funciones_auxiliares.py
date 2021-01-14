################# IMPORTS #####################################
from django.contrib.auth.models import User
from django.contrib import auth
###############################################################


#############################################
#Nombre Funcion: Chequear Usuario
#Tipo: Funcion auxiliar
#Funcionamiento: Revisa si el usuario existe en la BD
#Output: Retorna 0 en caso de exito, -1 en caso de contrario
#############################################
def check_user(request):    
    if ('email' in request.POST.keys()):#chequeamos que venga el campo en POST
        user_aux=User.objects.filter(username=request.POST['email'])#chequeamos que venga el campo en POST
        if user_aux.exists()==True:#Verificamos existencia
            return 0
    return -1


#############################################
#Nombre Funcion: Loguear user
#Tipo: Funcion auxiliar
#Funcionamiento: Revisamos si las credenciales del usuario son las correctas y lo logueamos
#Output: Retorna 0 en caso de exito, -1 en caso de contrario
#############################################
def loguear_user(request):
    if ('email' in request.POST.keys()) and ('pass' in request.POST.keys()):#chequeamos que venga el campo en POST
        user_aux=User.objects.filter(username=request.POST['email'])#chequeamos que venga el campo en POST
        if user_aux.exists()==False:#Verificamos existencia
            return -1
        user = auth.authenticate(username=request.POST['email'], password=request.POST['pass'])
        if user is not None and user.is_active:#Verificamos Logueo
            auth.login(request, user)
            return 0
    return -1
