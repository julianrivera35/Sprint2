from ..models import Historia
from django.views.decorators.csrf import csrf_exempt

def get_historia():
    historias = Historia.objects.all()
    return historias

def get_historia(historia_pk):
    historia = Historia.objects.get(pk= historia_pk)
    return historia

def update_historia(hisotria_pk, new_historia):
    historia = get_historia(hisotria_pk)
    historia.name = new_historia["name"]
    historia.descripcion = new_historia["descripcion"]
    historia.save()
    return historia

def create_historia(me):
    historia = Historia(name)
    