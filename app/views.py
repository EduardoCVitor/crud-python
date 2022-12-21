from django.shortcuts import render
from django.http import HttpResponse # Importa do django a função para responder um chamado de HTTP

# Create your views here.

def home(request):                      # Define a função Home que ao ser chamada
    return HttpResponse("Hello World")  # A resposta do HTTP retorna um Hello World
