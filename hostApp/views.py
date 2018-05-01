# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from hostApp import models

# Create your views here.
def usertype(request):
    data = models.UserType.objects.all()
    data1 = models.UserType.objects.all().values()
    data2 = models.UserType.objects.all().values_list()
    return render(request,'usertype.html',{'data':data,'data1':data1,'data2':data2})

def userinfo(request):
    if request.method == 'GET':
          userinfo = models.User.objects.all()
          userinfo1 = models.User.objects.all().values('name','age','user_type__caption')
          userinfo2 = models.User.objects.all().values_list('name','age','user_type__caption')
          return render(request,'userinfo.html',{'userinfo':userinfo,
                                                    'userinfo1':userinfo1,
                                                    'userinfo2':userinfo2
                                           })
    if request.method == 'POST':
        print 121313
        usernameinfo = request.POST.get('username')
        ageinfo = request.POST.get('age')
        usertypeinfo = request.POST.get('usertype_id')
        models.User.objects.create(name=usernameinfo,age=ageinfo,user_type_id=usertypeinfo)
        return  redirect('/hostApp/index/')

def hostinfo(request):
    hostobj = models.Host.objects.all()
    return render(request,'hostinfo.html',{'hostobj':hostobj})

def test_item(request):
    data = models.TestItem.objects.all()
    return render(request,'testitem.html',{'data':data})

def index(request):
    hostobj = models.Host.objects.all()
    UserType_data = models.UserType.objects.all()
    test_item_data = models.TestItem.objects.all()
    userinfo = models.User.objects.all()
    return render(request,'index.html',{'UserType_data':UserType_data,
                                        'test_item_data':test_item_data,
                                        'hostobj':hostobj,
                                        'userinfo':userinfo,
                                        })