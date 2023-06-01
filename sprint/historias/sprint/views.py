
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Esta es la página inicial de Widmy!!")

def HTMLSeleccionDeUsuario(request):
    contenido = """
    
    <!DOCTYPE html>
    <html>
    <head>
    <title>Iniciar Sesión</title>
    <style>
        body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        }
        .container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        text-align: center;
        }
        h1 {
        margin-top: 0;
        }
        .login-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 10px;
        cursor: pointer;
        }
    </style>
    </head>
    <body>
    <div class="container">
        <h1>Iniciar Sesión</h1>
        <p>Selecciona el tipo de cuenta con la que deseas iniciar sesión:</p>
        <button class="login-button" onclick="window.location.href='http://34.171.211.141:8080/login/auth0'">Médico</button>
        <button class="login-button" onclick="window.location.href='http://34.171.211.141:8080/admin'">Administrador</button>
    </div>
    </body>
    </html>
    
    
    """
    
    
    
    return HttpResponse(contenido)

def index(request):
   return render(request,'index.html')

