from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime
from pytz import timezone
from .managers import CustomUserManager
from django.contrib.auth.models import Group

dtz = timezone('America/Santiago').localize(datetime(2020, 9, 30, 23, 59, 59))

class RUTDVOptions(models.TextChoices):
    CERO = "0", _("0")
    UNO = "1", _("1")
    DOS = "2", _("2")
    TRES = "3", _("3")
    CUATRO = "4", _("4")
    CINCO = "5", _("5")
    SEIS = "6", _("6")
    SIETE = "7", _("7")
    OCHO = "8", _("8")
    NUEVE = "9", _("9")
    K = "K", _("K")


def validate_rut_dv(data):
    print(data)
    return "1"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, unique=True)
    first_name = models.CharField(_('nombres'), max_length=30, blank=True)
    last_name = models.CharField(_('apellidos'), max_length=30, blank=True)
    groups=models.ManyToManyField(Group,related_name='groups',blank=True)
    rut = models.IntegerField(_('rut'), validators=[MinValueValidator(500000), MaxValueValidator(100000000)], unique=True,blank=False, help_text="Sin dígito verificador")
    rut_dv = models.CharField(_('digito verificador'), validators=[validate_rut_dv], choices=RUTDVOptions.choices, default=RUTDVOptions.CERO, max_length=1 ,blank=False, help_text="Seleccione una opción")
    email = models.EmailField(_('email'), unique=True, blank=False)
    birthday = models.DateField(_('fecha de nacimiento'), blank=True, null=True, help_text="Quien autoriza la inscripción de este usuario")
    end_period = models.DateTimeField(_('expiración'), blank=False, help_text="Momento en que la cuenta expira (mínimo 15 minutos)", default=dtz)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('Usuario Activo'),default=True, help_text="Desactive para forzar expiración del usuario")
    is_staff = models.BooleanField(_('Es administrador'),default=False)
    supervisor = models.CharField(_('supervisor'), max_length=30, blank=True, help_text="En la unidad")
    authorization = models.CharField(_('autoriza'), max_length=50, blank=True, help_text="Quien autoriza la inscripción de este usuario (vacío si es el mismo supervisor)")
    position = models.CharField(_('cargo'), max_length=50, blank=True, help_text="En la unidad")
    department = models.CharField(_('unidad'), max_length=50, blank=True, help_text="Unidad en la cual trabaja")



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @property
    def is_authenticated(self):
        if timezone('America/Santiago').localize(datetime.today()) > self.end_period:
            self.is_active = False
        return self.is_active
