from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

"""
def hello(request, nome):
    return HttpResponse(f'<h1>Olá, {nome}!</h1>')
    
def adicao(request, num1, num2):
    resultado = num1 + num2
    return HttpResponse(f'A soma entre {num1} + {num2} = {resultado}')

def subtracao(request, num1, num2):
    resultado = num1 - num2
    return HttpResponse(f'A subtração entre {num1} - {num2} = {resultado}')

def divisao(request, num1, num2):
    resultado = num1 / num2
    return HttpResponse(f'A divisão entre {num1} / {num2} = {resultado:.2f}')

def multiplicacao(request, num1, num2):
    resultado = num1 * num2
    return HttpResponse(f'A multiplicação entre {num1} * {num2} = {resultado}')
    
"""
def lista_eventos(request):
    #evento = Evento.objects.get(id=1)
    usuario = request.user
    evento = Evento.objects.all()
    #evento = Evento.objects.filter(usuario=usuario)
    data = {'eventos': evento}
    return render(request, 'agenda.html', data)
