from django.shortcuts import render
from datetime import datetime
from .models import AlunoModel
from .forms import AvaliacaoForm

# Create your views here.
def palestra(request):
    palestra = [['Marketing Digital','Carlos','Lab01','26/11'],['Design Digital','Mariana','Lab03','26/11'],['Programação Web', 'Jonas','Lab01','27/11'],['Programação Orientada a Objetos','Jonas','Lab01','27/11'],['Pentest','Silmara','Lab03','27/11'],['Mineração de Dados','Amanda','Lab03','28/11'],['Lógica e Algoritmos para programação','Carlos','Lab01','28/11']]    
    contexto = {'Palestras': True, 'palestra': palestra}
    if len(palestra) > 0:

        return render(request,'templates.html',contexto)
    else:
        contexto = {'Palestras': False}
        return render(request, 'templates.html',contexto)


def cadastrar(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            AlunoModel.objects.create(**form.cleaned_data)
            contexto = {}
            return render(request,'cadastro.html', contexto)
        else:
            contexto = {'form': form}
            return render(request, 'cadastro.html', contexto)
    else:
        form = AvaliacaoForm()
        contexto = {'form': form}
        return render(request,'cadastro.html', contexto)

def listar(request):
    lista = AlunoModel
    contexto = {'Alunos': lista.nome}
    
    return render(request,'alunos.html', contexto)
    
