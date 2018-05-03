# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserType(models.Model):
    '''
    1、自动化测试人员
    2、RRU测试人员
    3、BBU测试人员
    4、领导
    5、其他部门人员
    '''
    caption = models.CharField(max_length=32)

class User(models.Model):
    '''
    周强  18   1
    '''
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    user_type = models.ForeignKey('UserType',to_field='id')

class Host(models.Model):
    envid = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(protocol='both',max_length=32,db_index=True)
    port = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    item = models.ForeignKey(to='TestItem',to_field='id')

class TestItem(models.Model):
    item = models.CharField(max_length=32)
    versionNum = models.CharField(max_length=32)

class Application(models.Model):
    name = models.CharField(max_length=32)
    r =models.ManyToManyField('Host')