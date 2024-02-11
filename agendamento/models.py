from django.db import models

# Create your models here.

class CadastroCliente(models.Model):
    nome_cliente = models.CharField(max_length = 200)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length = 20)
    cpf_cliente = models.CharField(max_length=11)


class CadastroPet(models.Model):
    nome_pet = models.CharField(max_length = 200)
    especie_pet = models.CharField(max_length = 200)
    sexo_pet = models.CharField(max_length = 15)
    cor_pet = models.CharField(max_length = 20)
    idade_pet = models.IntegerField()
    peso_pet = models.FloatField()
    cliente_pet = models.ForeignKey(CadastroCliente, on_delete = models.SET_NULL, null = True)

