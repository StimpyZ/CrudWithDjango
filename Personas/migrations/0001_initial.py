# Generated by Django 4.1 on 2022-09-04 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.PositiveBigIntegerField()),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
    ]
