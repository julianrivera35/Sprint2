from django.http import HttpResponse

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
        <button class="login-button" onclick="window.location.href='http://34.132.65.214:8080/login/auth0'">Médico</button>
        <button class="login-button" onclick="window.location.href='http://34.132.65.214:8080/admin'">Administrador</button>
    </div>
    </body>
    </html>
    
    
    """
    
    
    
    return HttpResponse(contenido)

def contenidoHTML(request):
    contenido = """ 
    <!DOCTYPE html>
<html>
<head>
  <title>Página de inicio - Hospital</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
    }
    .header {
      background-color: #f2f2f2;
      padding: 20px;
      text-align: right;
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
      margin-right: 20px;
    }
    .content {
      padding: 20px;
    }
    .doctor-images {
      display: flex;
      justify-content: center;
      margin-top: 30px;
    }
    .doctor-images img {
      width: 200px;
      margin: 10px;
    }
  </style>
</head>
<body>
  <div class="header">
    <a class="login-button" href="http://34.132.65.214:8080/inicio/">Iniciar sesión</a>
  </div>
  <div class="content">
    <h1>Bienvenido a Widmy</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>
    <div class="doctor-images">
      <img src="https://img.freepik.com/vector-gratis/ilustracion-concepto-doctores_114360-1515.jpg?w=1380&t=st=1683749448~exp=1683750048~hmac=f8dbfb317013900b993eb388eef7f8b97a97be18fd704558a80a9350c54835d5" alt="Doctor 1">
      <img src="https://img.freepik.com/vector-gratis/ilustracion-concepto-doctores_114360-1515.jpg?w=1380&t=st=1683749448~exp=1683750048~hmac=f8dbfb317013900b993eb388eef7f8b97a97be18fd704558a80a9350c54835d5" alt="Doctor 2">
      <img src="https://img.freepik.com/vector-gratis/ilustracion-concepto-doctores_114360-1515.jpg?w=1380&t=st=1683749448~exp=1683750048~hmac=f8dbfb317013900b993eb388eef7f8b97a97be18fd704558a80a9350c54835d5" alt="Doctor 3">
    </div>
  </div>
</body>
</html>
        
    """
    return HttpResponse(contenido)