# Generated by Django 3.0.5 on 2020-10-25 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Puntos',
        ),
        migrations.DeleteModel(
            name='Tipos',
        ),
    ]