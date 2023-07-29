# Generated by Django 4.2.3 on 2023-07-29 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0002_profesores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnos',
            name='fecha_nacimiento',
        ),
        migrations.RemoveField(
            model_name='profesores',
            name='fecha_nacimiento',
        ),
        migrations.AddField(
            model_name='profesores',
            name='experiencia',
            field=models.CharField(default=datetime.datetime(2023, 7, 29, 5, 31, 55, 3758, tzinfo=datetime.timezone.utc), max_length=32),
            preserve_default=False,
        ),
    ]
