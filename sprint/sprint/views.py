from django.http import HttpResponse

def home(request):
    return HttpResponse("Esta es la página inicial de Widmy!!")

def contenidoHTML(request):
    contenido = """ 

    <div style=" display: flex; align-items: center; justify-content: center;" class="login-box auth0-box before">
            <img style="width:80%; " src="/static/media/monitor.png" />
    </div>

    
    
    
    """
    return HttpResponse(contenido)