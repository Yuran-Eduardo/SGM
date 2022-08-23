from rest_framework.decorators import api_view
from django.shortcuts import render,redirect,reverse
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializers import RegisterSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Gestao.models import Categoria, Gestao
from Gestao.serializers import CategoriaSerializer, GestaoSerializer



def serialize_user(user):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })
        

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })


@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_data': serialize_user(user)
        })
    return Response({})

@api_view
def admin_category_view(request):
    return Response(request,#'nome do Template para o admin ver o form das categorias'
    )

@api_view
def admin_add_category_view(request):
    categoria = Categoria.objects.all()
    if request.method=='POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    return Response(serializer.data,{'serializer':serializer})

@api_view
def admin_view_category_view(request):
    categories = Categoria.objects.all()
    serializer = CategoriaSerializer(categories)
    return Response(serializer.data,{'categories':categories})