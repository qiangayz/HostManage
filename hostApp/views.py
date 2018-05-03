# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
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

def test_ajax(request):
    result = {
        'status':True,
        'error':None,
        'data':None
    }
    try:
        print "===>",request.POST
        #if request.method=="POST":
        host=request.POST.get('hostname')
        ipinfo=request.POST.get('ip')
        port=request.POST.get('port')
        username=request.POST.get('usernameinfo')
        password=request.POST.get('passwordinfo')
        item=request.POST.get('iteminfo')
        if host and len(host)>5:
            models.Host.objects.create(
                envid=host,
                ip=ipinfo,
                port=port,
                username=username,
                password=password,
                    item_id=item
            )
        else:
            result['status'] = False
            result['error'] = '太短了'
    except Exception as e:
        result['status'] = False
        result['error'] = '输入错误'
    return  HttpResponse(json.dumps(result))

def test_ajax1(request):
    print "===>", request.POST
    result = {
        'status': True,
        'error': None,
        'data': None
    }
    if request.POST.get('tablename')=='host':
        hid = request.POST.get('hid')
        models.Host.objects.filter(id=hid).delete()

    if request.POST.get('tablename')=='application':
        appid = request.POST.get('appid')
        models.Application.objects.filter(id=appid).delete()
    return HttpResponse(json.dumps(result))

def edit_data(request,hid):
    if request.method=="GET":
        print hid
        data=models.Host.objects.filter(id=hid).first()
        test_item_data = models.TestItem.objects.all()
        print data.envid,data.ip,test_item_data
        return render(request,'editHost.html',{
                                              'data':data,
                                             'data1':test_item_data
                                          })
    if request.method=="POST":
        print '===>>',request.POST
        envid= request.POST.get('envid')
        ipinfo= request.POST.get('ip')
        portinfo= request.POST.get('port')
        usernameinfo= request.POST.get('username')
        passinfo= request.POST.get('password')
        item= request.POST.get('iteminfo')
        obj=models.Host.objects.filter(id=hid)
        print obj
        obj.update(envid=envid,ip=ipinfo,port=portinfo,username=usernameinfo,password=passinfo,item_id=item)
        return  redirect('/hostApp/index')

def many_to_many(request):
    print request.POST
    appname=request.POST.get('appname')
    hostlist= request.POST.getlist('hostlist')
    print appname,hostlist
    obj=models.Application.objects.create(name=appname)
    obj.r.add(*hostlist)
    return  HttpResponse('123123123')

def index(request):
    hostobj = models.Host.objects.all()
    UserType_data = models.UserType.objects.all()
    test_item_data = models.TestItem.objects.all()
    userinfo = models.User.objects.all()
    appinfo = models.Application.objects.all()
    return render(request,'index.html',{'UserType_data':UserType_data,
                                        'test_item_data':test_item_data,
                                        'hostobj':hostobj,
                                        'userinfo':userinfo,
                                        'appinfo':appinfo
                                        })