from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from RiskmapApp import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),#Url para admin
    path('',include('dashboard.urls')),#URL para vista no logueado
    path('login/',include('login.urls')),#url vista login
    path('user/',include('userprofiles.urls')),#url vista logueado
    ###Estas vistas eran del proyecto original del profesor Victor Codocedo, las conservamos por que podrían ser de futuro uso
    #url(r'^$', views.damap, name='RiskMapApp'),
    #url(r'^tdata/', views.territorial_data, name='Territorial Data'),
    #url(r'^sdata/', views.sensitive_data, name='Sensitive Data'),
    #url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    #url(r'^logout/$', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
