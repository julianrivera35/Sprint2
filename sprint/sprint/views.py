from django.http import HttpResponse

def home(request):
    return HttpResponse("Esta es la página inicial de Widmy!!")