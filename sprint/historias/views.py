from .logic import historias_logic as me
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
def historias_view(request):
    
    
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            historia_dto = me.get_historia(id)
            historia = serializers.serialize('json', [historia_dto,])
            return HttpResponse(historia, 'application/json')
        else:
            historias_dto = me.get_historias()
            historias = serializers.serialize('json', historias_dto)
            return HttpResponse(historias, 'application/json')

    if request.method == 'POST':
        historia_dto = me.create_historia(json.loads(request.body))
        historia = serializers.serialize('json', [historia_dto,])
        return HttpResponse(historia, 'application/json')

    
    #if request.method == 'DELETE':
    #    pk = request.GET.get("id", None)
    #    historia_dto = me.historia_delete(pk)
    #    historia = serializers.serialize('json',[historia_dto,])
    #    return HttpResponse('application/json')

@login_required
def historia_view(request, pk):
    
    
    if request.method == 'GET':
        historia_dto = me.get_historia(pk)
        historia = serializers.serialize('json', [historia_dto,])
        return HttpResponse(historia, 'application/json')

    if request.method == 'PUT':
        historia_dto = me.update_historia(pk, json.loads(request.body))
        historia = serializers.serialize('json', [historia_dto,])
        return HttpResponse(historia, 'application/json')

    
    #if request.method == 'DELETE':
    #    historia_dto = me.historia_delete(pk)
    #    historia = serializers.serialize('json',[historia_dto,])
    #    return HttpResponse('application/json')

# Create your views here.
