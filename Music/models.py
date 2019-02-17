# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Info(models.Model):
    song = models.CharField(max_length=64, blank=True, null=True)
    size = models.CharField(max_length=64, blank=True, null=True)
    link = models.CharField(max_length=256, blank=True, null=True)
    sid = models.ForeignKey('Singer', models.DO_NOTHING, db_column='sid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info'


class Singer(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    nid = models.ForeignKey(Category, models.DO_NOTHING, db_column='nid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'singer'
