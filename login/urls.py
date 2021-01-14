from django.conf.urls import url,include
from login.views import *

urlpatterns= [
	url(r"^$",login),#Vista login	
]
