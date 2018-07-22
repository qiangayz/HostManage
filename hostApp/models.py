# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class UserType(models.Model):
    caption = models.CharField(max_length=32)


class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    user_type = models.ForeignKey('UserType', to_field='id')


class Host(models.Model):
    envid = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol='both', max_length=32, db_index=True)
    port = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    item = models.ForeignKey(to='TestItem', to_field='id')


class TestItem(models.Model):
    item = models.CharField(max_length=32)
    versionNum = models.CharField(max_length=32)


class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField('Host')
