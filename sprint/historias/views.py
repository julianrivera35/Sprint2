from .logic import historias_logic as me
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required
from sprint.auth0backend import getRole
from .logic.historias_logic import get_historias, get_historia, create_historia
from django.shortcuts import render
from .forms import HistoriaForm
from django.contrib import messages


@login_required
def historia_list(request):
   role = getRole(request)
   if role == "Medico":
      historias = get_historias()
      context={'historias_list': historias }
      return render(request, 'Historia/historias.html',context)
   else:
      return HttpResponse("Unauthorized User")

@login_required
def single_historia(request,id=0):
   historia = get_historia(id)
   context = {
       'historia':historia
   }
   return render(request, 'historia.html', context)

@login_required
def historia_create(request):
    role = getRole(request)
    if role == "Medico":
        if request.method == 'POST':
            form = HistoriaForm(request.POST)
            if form.is_valid():
                create_historia(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created historia')
                return HttpResponseRedirect(reverse('historiacreate'))
            else:
                print(form.errors)
        else:
            form = HistoriaForm()

        context = {
            'form': form,
        }
        return render(request, 'Historia/historiaCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")

    
# Create your views here.
