from django import forms
from django.contrib.auth.models import User
from . import models



class CategoriaForm(forms.ModelForm):
    class Meta:
        model=models.Categoria
        fields=['category_name']

class ImpostosForm(forms.ModelForm):
    categoria=forms.ModelChoiceField(queryset=models.Categoria.objects.all(),empty_label="Category Name", to_field_name="id")
    class Meta:
        model=models.Policy
        fields=['nome_imposto','quantia','parcela',]