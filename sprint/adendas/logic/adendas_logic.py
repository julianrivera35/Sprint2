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
    adenda = Adenda(name = me["name"], descripcion = ["descripcion"], adenda=["adenda"])
    adenda.save()
    return adenda

def adendas_view(request):
    if request.method == 'GET':
        adendas = me.get_adendas()
        adendas_dto = serializers.serialize('json',  adendas)
        return HttpResponse(adendas_dto, 'application/json')
    
    
@csrf_exempt
def adendas_view(request, pk):
    if request.method == 'GET':
        adenda_dto = me.get_adenda(pk)
        adenda = serializers.serialize('json',[adenda_dto,])
        return HttpResponse(adenda, 'appliaction/json')
    
    if request.method == 'PUT':
        adenda_dto = me.update_adenda(pk, json.loads(request.boy))
        adenda = serializers.serialize('json',[adenda_dto,])
        return HttpResponse(adenda, 'application/json')
    
@csrf_exempt
def adenda_views(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            adenda_dto = me.get_adenda(id)
            adenda = serializers.serialize('json',[adenda_dto,])
            return HttpResponse(adenda, 'apllication/json')
        else:
            adendas_dto = me.create_adenda(json.loads(request.body))
            adenda = serializers.serialize('json', adendas_dto)
            return HttpResponse(adenda, 'application/json')
        
    if request.method == 'POST':
        adenda_dto = me.create_adenda(json.loads(request.body))
        adenda = serializers.serialize('json', [adenda_dto,])
        return HttpResponse(adenda, 'application/json')