from statistics import mode
from rest_framework.decorators import api_view
from django.shortcuts import render,redirect,reverse
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication

from Gestao import models
from Gestao.forms import ImpostosForm
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

@api_view(['GET'])
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()



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

@api_view(['GET'])
def admin_category_view(request):
    return Response(request)

@api_view(['POST'])
def admin_add_category_view(request):
    categoria = Categoria.objects.all()
    serializer = CategoriaSerializer(categoria)
    if request.method=='POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    return Response(serializer.data,{'serializer':serializer})

@api_view(['GET'])
def admin_view_category_view(request):
    categories = Categoria.objects.all()
    serializer = CategoriaSerializer(categories, many=True)
    return Response(serializer.data,{'serializer':serializer})

@api_view(['POST'])
def delete_category_view(request,pk):
    categoria = models.Categoria.objects.get(id=pk)
    categoria.delete()
    serializer = CategoriaSerializer(categoria, data=request.data)
    return Response(serializer.data)

@api_view(['POST'])
def admin_update_category_view(request):
    categorias = models.Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, data=request.data)
    return Response(serializer.data)

@api_view(['GET'])
def admin_imposto_view(request):
    impostos = models.Gestao(impostos)
    serializer = GestaoSerializer(impostos)
    return Response(serializer.data)

@api_view(['POST'])
def admin_add_imposto_view(request):
    impostos = models.Gestao.objects.all()
    serializer = GestaoSerializer(impostos)
    if serializer.method=='POST':
        serializer = GestaoSerializer(impostos, data=request.data)
        if serializer.is_valid():
            categoryid = request.POST.get('category')
            category = models.Categoria.objects.get(id=categoryid)
            imposto = serializer.save(commit=False)
            imposto.category=category
            imposto.save()
            return Response(serializer.data, status=201)
    return Response(serializer.data,{'serializer':serializer})

@api_view(['POST'])
def admin_view_imposto_view(request):
    impostos = models.Gestao.objects.all()
    serializer = CategoriaSerializer(impostos)
    return Response(serializer.data, status=201)
@api_view(['GET'])
def admin_update_policy_view(request):
    impostos = models.Gestao.objects.all()
    serializer = models.Gestao.objects.all(impostos)
    return Response(serializer.data,{'serializer':serializer})

@api_view(['POST'])
def update_imposto_view(request,pk):

    imposto = models.Gestao.objects.get(id=pk)
    serializer=GestaoSerializer(instance=imposto)
    
    if request.method=='POST':
        serializer=GestaoSerializer(data=request.data,instance=policy)
        
        if serializer.is_valid():

            categoryid = request.POST.get('category')
            category = models.Categoria.objects.get(id=categoryid)
            imposto = serializer.save(commit=False)
            imposto.category=category
            imposto.save()
           
            return Response(serializer.data, status=201)
    return Response(serializer.data,{'serializer':serializer})

