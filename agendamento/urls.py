from django.urls import path
from agendamento.views import AgendamentoDetailCliente, AgendamentoListCliente,AgendamentoDetailPet,AgendamentoListPet

urlpatterns = [
    path('client-register', AgendamentoListCliente.as_view()),
    path('cliente/<int:pk>/', AgendamentoDetailCliente.as_view()),

    path('pet-register', AgendamentoListPet.as_view()),
    path('pet/<int:pk>/', AgendamentoDetailPet.as_view())

]
