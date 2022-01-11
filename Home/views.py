from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from decouple import config
import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.db import models
from dynamic_models.models import ModelSchema, FieldSchema
from django.urls import clear_url_caches
from importlib import import_module, reload
from django.contrib import admin
from django.conf import settings
from .models import Modelnames

# Create your views here.


def base2(request):
    return render(request, 'base2.html')


def addModelEntries(request):
    return redirect('/admin')

def createModels(request):
    modelExists = False
    modelCreated = False
    modelName = ''
    if request.POST:
        modelName = request.POST['modelname']
        try:
            model_schema = ModelSchema.objects.create(
                name=request.POST['modelname'])
            modelCreated = True
        except Exception as e:
            modelExists = True
            return render(request, 'createModels.html', context={'modelExists': modelExists, 'modelCreated': modelCreated, 'modelName': modelName})
        len_req = (len(request.POST) - 2) // 5
        count = 0
        for x in range(len_req):
            count = count + 1
            field_schema = FieldSchema.objects.create(
                name=request.POST['field' + str(count)],
                data_type=request.POST['datatype' + str(count)],
                model_schema=model_schema,
                max_length=request.POST['maxlen' + str(count)],
                null=request.POST['null' + str(count)],
                unique=request.POST['unique' + str(count)]
            )
        model_create = Modelnames.objects.create(
            modelname=request.POST['modelname'])
        reg_model = model_schema.as_model()
        admin.site.register(reg_model)
        reload(import_module(settings.ROOT_URLCONF))
        clear_url_caches()
    return render(request, 'createModels.html', context={'modelExists': modelExists, 'modelCreated': modelCreated, 'modelName': modelName})


def showObjectLists(request):
    modelNamesQuerySet = Modelnames.objects.all()
    modelNames = list()
    for model in modelNamesQuerySet:
        modelNames.append(model.modelname)
    cont_dict = {
        'modelNames': modelNames,
        'get': True
    }
    if request.POST:
        model = ModelSchema.objects.get(
            name=request.POST['modelname']).as_model()
        objList = model.objects.all().values()
        fieldNames = list()
        noEntry = False
        try:
            for x in objList[0]:
                fieldNames.append(x)
        except Exception as e:
            noEntry = True
        cont_dict = {
            'modelNames': modelNames,
            'objects': objList,
            'noEntry': noEntry,
            'fieldNames': fieldNames,
            'objectType': request.POST['modelname'],
            'get': False
        }
    return render(request, 'displayObjects.html', context=cont_dict)


def test(request):
    modelNamesQuerySet = Modelnames.objects.all()
    modelNames = list()
    for model in modelNamesQuerySet:
        modelNames.append(model.modelname)
    cont_dict = {
        'modelNames': modelNames,
        'get': True
    }
    if request.POST:
        model = ModelSchema.objects.get(
            name=request.POST['modelname']).as_model()
        objList = model.objects.all().values()
        fieldNames = list()
        noEntry = False
        try:
            for x in objList[0]:
                fieldNames.append(x)
        except Exception as e:
            noEntry = True
        cont_dict = {
            'modelNames': modelNames,
            'objects': objList,
            'noEntry': noEntry,
            'fieldNames': fieldNames,
            'objectType': request.POST['modelname'],
            'get': False
        }
    return render(request, 'test.html', context=cont_dict)




# Create your views here.

def index(request):
    return render(request,'index.html')



def profile(request):
    user=request.user

    auth0_user=user.social_auth.get(provider='auth0')

    user_data={
        'user_id':auth0_user.uid,
        'name':user.first_name,
        'picture':auth0_user.extra_data['picture']
    }

    context={
        'user_data':json.dumps(user_data,indent=4),
        'auth0_user':auth0_user
    }


    return render(request,'profile.html',context)

#logout
# https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}

def logout(request):
    django_logout(request)

    domain=config('APP_DOMAIN')
    client_id=config('APP_CLIENT_ID')
    return_to='http://127.0.0.1:8000/'

    return HttpResponseRedirect(f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")