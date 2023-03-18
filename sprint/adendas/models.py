from django.db import models
from sprint.historias.models import Historia

class Adenda(models.Model):
    name = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 500)
    historia = models.ManyToManyField(Historia)
    dateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.name, self.descripcion)
    

# Create your models here.
