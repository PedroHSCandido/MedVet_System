from rest_framework import generics

from agendamento.models import CadastroCliente, CadastroPet
from agendamento.serializers import ClienteSerializer, PetSerializer

# Create your views here.

class AgendamentoDetailCliente(generics.RetrieveUpdateDestroyAPIView): 
    queryset = CadastroCliente.objects.all() 
    serializer_class = ClienteSerializer

class AgendamentoListCliente(generics.ListCreateAPIView): 
    queryset = CadastroCliente.objects.all()
    serializer_class = ClienteSerializer

#________________________________________________________________________________#

class AgendamentoDetailPet(generics.RetrieveUpdateDestroyAPIView): 
    queryset = CadastroPet.objects.all() 
    serializer_class = PetSerializer

class AgendamentoListPet(generics.ListCreateAPIView): 
    queryset = CadastroPet.objects.all()
    serializer_class = PetSerializer
    