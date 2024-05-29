# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AccidentesHmo(models.Model):
    anio = models.IntegerField(primary_key=True)
    numero_mes = models.IntegerField()
    mes = models.TextField()
    tipo_accidente = models.TextField()
    estado = models.TextField()
    nombre_municipio = models.TextField()
    total_accidentes = models.IntegerField()
    suma_muertos = models.IntegerField()
    suma_heridos = models.IntegerField()
    class Meta:
        db_table = 'accidentes_transito_hmo_2012_2021'  # Nombre de la tabla en MySQL
        managed = False

