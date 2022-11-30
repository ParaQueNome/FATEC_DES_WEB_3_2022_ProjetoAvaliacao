from django.shortcuts import render

# Create your views here.
def palestra(request):
    palestra = [['Marketing Digital','Carlos','Lab01','26/11'],['Design Digital','Mariana','Lab03','26/11'],['Programação Web', 'Jonas','Lab01','27/11'],['Programação Orientada a Objetos','Jonas','Lab01','27/11'],['Pentest','Silmara','Lab03','27/11'],['Mineração de Dados','Amanda','Lab03','28/11'],['Lógica e Algoritmos para programação','Carlos','Lab01','28/11']]    
    contexto = {'Palestras': palestra}
    if len(palestra) > 0:

        return render(request,'templates.html',contexto)
    else:
        contexto = {'Palestras': False}
        return render(request, 'templates.html',contexto)
