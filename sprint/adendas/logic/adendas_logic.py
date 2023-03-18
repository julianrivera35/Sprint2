from ..models import Adenda
from django.views.decorators.csrf import csrf_exempt

def get_adenda():
    adendas = Adenda.objects.all()
    return adendas

def get_adenda(adenda_pk):
    adenda = Adenda.objects.get(pk= adenda_pk)
    return adenda

def update_adenda(adenda_pk, new_adenda):
    adenda = get_adenda(adenda_pk)
    adenda.name = new_adenda["name"]
    adenda.descripcion = new_adenda["descripcion"]
    adenda.save()
    return adenda

def create_adenda(me):
    adenda = Adenda(name)