from django.db import models

# Create your models here.
class Categoria(models.Model):
    category_name = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name

class Gestao(models.Model):
    category = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    nome_imposto = models.CharField(max_length=100)
    quantia = models.PositiveIntegerField()
    parcelas = models.PositiveIntegerField()
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.nome_imposto
    
    