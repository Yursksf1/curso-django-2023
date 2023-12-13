# Generated by Django 4.2.7 on 2023-11-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoId', models.CharField(max_length=10)),
                ('nrohoras', models.PositiveIntegerField()),
                ('valorhoras', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.PositiveIntegerField()),
                ('altura', models.DecimalField(decimal_places=2, default=165.0, max_digits=5)),
                ('peso', models.DecimalField(decimal_places=2, default=80.0, max_digits=5)),
                ('tipoclasificacion', models.CharField(max_length=10)),
                ('horas', models.PositiveIntegerField(default=30)),
            ],
        ),
    ]