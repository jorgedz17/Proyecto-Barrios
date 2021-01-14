from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name','rut', 'rut_dv')
    list_filter = ('username', 'first_name', 'last_name','rut','rut_dv')
    fieldsets = (
        ("Login", {'fields': ('username', 'password', 'is_active', 'is_staff', 'end_period', 'groups')}),
        ("Información Personal", {'fields': ('first_name','last_name','email', ('rut', 'rut_dv'), 'birthday')}),
        ("Información Laboral", {'fields': ('department', 'position', 'supervisor','authorization')}),
    )
    add_fieldsets = (
        ("Login", {'classes': ('wide',), 'fields': ('username', 'password1', 'password2', 'is_active', 'is_staff', 'end_period', 'groups')}),
        ("Información Personal", {'fields': ('first_name','last_name','email', ('rut', 'rut_dv'),'birthday')}),
        ("Información Laboral", {'fields': ('department','position', 'supervisor','authorization')}),
        # (None, {
        #     'classes': ('wide',),
        #     'fields': ('username','first_name', 'last_name','email', 'rut', 'password1', 'password2')}
        # ),
    )
    search_fields = ('username',)
    ordering = ('username',)


#admin.site.register(CustomUser, CustomUserAdmin)
