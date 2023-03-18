from django.db import models
from historias.models import Historia

class Adenda(models.Model):
    name = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 500)
    separador = " Historia: "
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE, default=False)
    dateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s %s %s' % (self.name, self.descripcion,self.separador ,self.historia)
    

# Create your models here.
