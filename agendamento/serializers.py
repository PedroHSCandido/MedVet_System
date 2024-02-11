from rest_framework import serializers
from agendamento.models import CadastroCliente, CadastroPet

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroCliente
        fields = ['id', 'nome_cliente', 'email_cliente', 'telefone_cliente', 'cpf_cliente']

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroPet
        fields = ['id', 'nome_pet','especie_pet','sexo_pet','cor_pet', 'idade_pet', 'peso_pet', 'cliente_pet',]

