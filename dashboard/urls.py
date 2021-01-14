from django.conf.urls import url,include
from dashboard.views import *

urlpatterns= [
	url(r"^$",index),#Vista de inicio
	url(r"^about/$",about),#Vista de sobre nosotros
	url(r"^data/$",territorial_data),#Vista de los datos de las zonas serializada
	url(r"^markers/$",markers_data),#Vista de los markers de la BD serializada	
]
