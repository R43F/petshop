from django.shortcuts import render
from .models import Estoque


def home(request):
    return render(request, 'home.html')


def estoque(request):
    estoque = Estoque.objects.all()
    template_name = 'estoque.html'
    context = {
        'estoque': estoque
    }
    return render(request, template_name, context)


def agendamento(request):
    return render(request, 'agendamento.html')
