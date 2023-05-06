from django.http import HttpResponse

def home(request):
    return HttpResponse("Esta es la página inicial de Widmy!!")

def contenidoHTML(request):
    contenido = """ 
    <html>
    <head>
    <style type= "text/css"> div{background-color:3BEED5; width: 100%; height: 100px; font-weight:bold; padding: 5px;}
    </style>
    </head>
    <body>
    <div><center><font size=30>Widmy</font></center></div>
    <h1> <font size=15>Como eres un paciente en realidad no tienes acceso a nada por acá </font></h1>
    <img src="https://i.pinimg.com/550x/62/21/4e/62214ea9432fef2ca9974ef274d0924b.jpg" width="500" height="500">
    </body>
    </html>
    
    
    """
    return HttpResponse(contenido)