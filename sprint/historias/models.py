from django.db import models

class Historia(models.Model):
    name = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 500)
    adenda = models.ForeignKey(Adenda, on_delete=models.CASCADE, default= None)
    dateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.name, self.descripcion)
    
    
    
# Create your models here.
