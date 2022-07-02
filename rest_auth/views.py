from venv import create
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    try:
        data = JSONParser().parse(request)
    
        username = data['username']
        password = data['password']
    except:
        return Response("Campos del Body deben ser username y password")
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario no se encuentra en los registros")
    
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Contraseña incorrecta, intente nuevamente.")
    token, create = Token.objects.get_or_create(user=user)
    return Response(token.key)

# Create your views here.
