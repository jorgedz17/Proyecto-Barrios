from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from itertools import cycle
from .models import CustomUser

def get_verifier_digit(rut):
    '''
    Validador de ruts obtenido desde
    https://gitlab.labcomp.cl/mti/mtisp/blob/e6c3b1e28ad19f7d8b565194e878df013a135054/mti/applicants/validators.py
    '''
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    suma = sum(d * f for d, f in zip(reversed_digits, factors))
    dv = 'K' if (-suma) % 11 == 10 else (-suma) % 11
    return dv


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name',)
        widgets = {
             'rut': forms.NumberInput(attrs={'style': 'width: 100px'}),
            }
    def clean(self):
        super(UserCreationForm, self).clean()
        # This method will set the `cleaned_data` attribute

        rut = self.cleaned_data.get('rut')
        rut_dv = self.cleaned_data.get('rut_dv')

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password1 == password2:
            raise ValidationError('Passwords must match')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name',)
        widgets = {
             'rut': forms.NumberInput(attrs={'style': 'width: 100px'}),
            }
    def clean(self):
        super(UserChangeForm, self).clean()
        # This method will set the `cleaned_data` attribute

        rut = self.cleaned_data.get('rut')
        rut_dv = self.cleaned_data.get('rut_dv')
        if get_verifier_digit(rut) != rut_dv:
            raise forms.ValidationError("Digito Verificador no coincide con el RUT ingresado")
        # print(rut, rut_dv, )
