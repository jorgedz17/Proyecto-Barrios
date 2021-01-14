from django.conf.urls import url,include
from userprofiles.views import *

urlpatterns= [
	url(r"^$",index),#vista incial usuario	
	url(r"^logout/$",logout_),#vista para cerrar sesion
]
