from django.shortcuts import render

# Create your views here.
def palestra(request):
    return render(request, 'templates.html')
    