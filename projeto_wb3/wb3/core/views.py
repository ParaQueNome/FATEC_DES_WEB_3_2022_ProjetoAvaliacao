from django.shortcuts import render

# Create your views here.
def palestra(request):
    palestra = ['Marketing Digital','Design Digital','Programação Web','Programação Orientada a Objetos','Pentest','Mineração de Dados','Lógica e Algoritmos para programação']    
    contexto = {'Palestras': palestra}
    return render(request,'templates.html',contexto)