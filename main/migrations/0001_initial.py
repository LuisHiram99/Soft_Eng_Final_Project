# Generated by Django 5.0.6 on 2024-05-28 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccidentesTransitoHmo20122021',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('numero_mes', models.IntegerField()),
                ('mes', models.TextField()),
                ('tipo_accidente', models.TextField()),
                ('estado', models.TextField()),
                ('nombre_municipio', models.TextField()),
                ('total_accidentes', models.IntegerField()),
                ('suma_muertos', models.IntegerField()),
                ('suma_heridos', models.IntegerField()),
            ],
            options={
                'db_table': 'AccidentesTransitoHmo20122021',
                'managed': False,
            },
        ),
    ]
