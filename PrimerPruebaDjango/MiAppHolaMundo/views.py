from django.http import HttpResponse

def saludar(request):
    return HttpResponse('Holaaaaa Mundo')

def despedida(request):
    return HttpResponse('Chauuuuuuu Mundo')