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
    historia = Historia(name = me["name"], descripcion = ["descripcion"])
    historia.save()
    return historia

def historias_view(request):
    if request.method == 'GET':
        historias = me.get_historias()
        historias_dto = serializers.serialize('json',  historias)
        return HttpResponse(historias_dto, 'application/json')
    
    
@csrf_exempt
def historia_view(request, pk):
    if request.method == 'GET':
        historia_dto = me.get_historia(pk)
        historia = serializers.serialize('json',[historia_dto,])
        return HttpResponse(historia, 'appliaction/json')
    
    if request.method == 'PUT':
        historia_dto = me.update_historia(pk, json.loads(request.boy))
        historia = serializers.serialize('json',[historia_dto,])
        return HttpResponse(historia, 'application/json')
    
    #if request.method == 'DELETE':
    #    historia_dto = me.historia_delete(pk)
    #    historia = serializers.serialize('json',[historia_dto,])
    #    return HttpResponse('application/json')
    
@csrf_exempt
def historia_views(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            historia_dto = me.get_historia(id)
            historia = serializers.serialize('json',[historia_dto,])
            return HttpResponse(historia, 'apllication/json')
        else:
            historia_dto = me.create_historia(json.loads(request.body))
            historia = serializers.serialize('json', historia_dto)
            return HttpResponse(historia, 'application/json')
        
    if request.method == 'POST':
        historia_dto = me.create_historia(json.loads(request.body))
        historia = serializers.serialize('json', [historia_dto,])
        return HttpResponse(historia, 'application/json')
    
    #if request.method == 'DELETE':
    #    pk = request.GET.get("id", None)
    #    historia_dto = me.historia_delete(pk)
    #    historia = serializers.serialize('json',[historia_dto,])
    #    return HttpResponse('application/json')