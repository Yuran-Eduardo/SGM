from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User

from Gestao.models import Categoria, Gestao

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','first_name','last_name')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class CategoriaSerializer(serializers.ModelSerializer):
    class meta:
        model = Categoria
        fields = ['category_name']

class GestaoSerializer(serializers.ModelSerializer):
    class meta:
        model = Gestao
        fields = ['category','nome_imposto','parcelas','quantia']