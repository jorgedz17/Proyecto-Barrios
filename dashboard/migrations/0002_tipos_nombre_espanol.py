# Generated by Django 3.0.6 on 2020-11-09 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipos',
            name='nombre_espanol',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
