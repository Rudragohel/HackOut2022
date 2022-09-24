from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from ServeGoal_app.models import User


def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def display_register(request):
    template = loader.get_template('register.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('login.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def verify_user(request):
    template = loader.get_template('login.html')
    print("Here")
    received_email = request.POST.get("user_email")
    received_password = request.POST.get("user_password")
    print(received_email, received_password)
    found = User.objects.get(email=received_email)
    if found.password == received_password:
        template = loader.get_template('index.html')
        context = {
            "name": "Hi, " + found.name,
            "LoginSuccess": True,
        }

    else:
        context = {
            "LoginFail": True
        }
    return HttpResponse(template.render(context, request))

def create_user(request):
    template = loader.get_template('index.html')
    print("Here")
    received_name = request.POST.get("user_name")
    received_email = request.POST.get("user_email")
    received_password = request.POST.get("user_password")
    print(received_name,received_email, received_password)
    new_user=User(name=received_name,email=received_email,password=received_password)
    new_user.save()
    context = {

    }
    return HttpResponse(template.render(context, request))
