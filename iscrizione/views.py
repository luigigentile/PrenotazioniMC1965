from django.http import HttpResponseRedirect,HttpResponseBadRequest
from django.urls import reverse,reverse_lazy
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator # ,EmptyPage,PageNotAnInteger
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import resolve

from django.core.paginator import Paginator

from django.db.models import Count


import datetime

import json
import requests


import os
import subprocess

# Create your views here.
from .forms import IscrizioneModelForm,EventoModelForm,TabellaFermateModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from iscrizione.models import Eventi,TabellaFermate,Iscrizioni,AnagraficaNominativi

from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView

from django.core.cache import cache



#    AGGIUNTE EFFETTUATE PER BASILIO
# Create your views here.
#    AGGIUNTE EFFETTUATE PER BASILIO

def creaSimulazione(request):
    from pathlib import Path
#    import sys
    import os
    import subprocess
    import shutil

    print("richiesta")
    print(request)
    if request.method == "POST":
        form = SimulazioneForm(request.POST)
        if form.is_valid():
            simulazione = form.save(commit=False)
            simulazione.save()
            success_url = reverse_lazy('lista_eventi')
            return HttpResponseRedirect(success_url)
#            return HttpResponseRedirect('/')

    else:
        print("creo simulazione")
        sandobox_dir = '/mnt/c/lavori/GitHub/CircuitMindRepositories/sandbox'
        sandobox_dir = 'C:\Lavori\GitHub\CircuitMindRepositories\sandbox'
        os.chdir(sandobox_dir)
        #   RUN THE power_achitect script in a subprocess
        subprocess.run("python power/power_architect_original.py",shell=True)
        lista_nominativi = AnagraficaNominativi.objects.all()
        context = {'lista_nominativi':lista_nominativi}
        return render(request,"iscrizione/crea_simulazione.html",context)

#  FINE AGGIUNTE PER BASILIO




class CancellaIscrizione(DeleteView):
    model = Iscrizioni
#    success_url="/"
#    success_url = reverse_lazy('user_iscrizioni_list')
#    success_url = reverse_lazy('user_iscrizioni_list_for_evento',kwargs={'pk':1})
##    template_name = "iscrizione/iscrizione_confirm_delete.html"
    template_name = "iscrizione/confirm_delete.html"
    context_object_name = 'iscrizione_da_eliminare'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['avviso'] = "Confermi di voler eliminare la seguente Iscrizione?"
            return context

    def get_success_url(self,**kwargs):
        evento =cache.get('evento')
        return reverse_lazy('user_iscrizioni_list_for_evento',kwargs={'pk':evento})


class UpdateIscrizione(UpdateView):
    model = Iscrizioni
    fields = ['nome','cognome','telefono','id_fermata']
    template_name = "iscrizione/update_iscrizione.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        evento=self.kwargs.get("pk")
        context['iscrizioni'] = Iscrizioni.objects.all()
        return context

    def get_success_url(self,**kwargs):
        evento = cache.get('evento')
        return reverse_lazy('user_iscrizioni_list_for_evento',kwargs={'pk':evento})


class UserIscrizioniListForEvento(ListView,LoginRequiredMixin):
    model = Iscrizioni
#    paginate_by =10
    template_name = 'iscrizione/UserIscrizioniList.html'
    context_object_name = 'useriscrizioni'

    def get_queryset(self,*args,**kwargs):
        user_id=self.request.user.id
        evento=self.kwargs.get("pk")
        if evento == 0:
            qset= Iscrizioni.objects.filter(id_user=user_id)
        else:
            qset= Iscrizioni.objects.filter(id_user=user_id,id_evento=evento)
        return qset

    def get_context_data(self, **kwargs):
            # Call the base implementation first to get the context
            context = super().get_context_data(**kwargs)
            evento=self.kwargs.get("pk")
            cache.set('evento', evento, 30)
            print(evento)
            context['eventi'] = Eventi.objects.all()
            context['pkevento']= evento
            return context


class UserIscrizioniList(ListView,LoginRequiredMixin):
    model = Iscrizioni
    paginate_by =6
    template_name = 'iscrizione/UserIscrizioniList.html'
    context_object_name = 'useriscrizioni'

    def get_queryset(self,*args):
        user_id=self.request.user.id
        qsuseriscrizioni= Iscrizioni.objects.filter(id_user=user_id).order_by('-id_evento_id')
        return qsuseriscrizioni

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['eventi'] = Eventi.objects.all()
        return context


class EventList(ListView,LoginRequiredMixin):
    model = Eventi
    paginate_by =5
    template_name = 'iscrizione/lista_eventi.html'
    context_object_name = 'eventi'

    def get_queryset(self,*args):

#        queryseteventi=Eventi.objects.all
        queryseteventi= Eventi.objects.filter(data_evento__gt=datetime.datetime.now())
        return queryseteventi

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_list = Eventi.objects.all()
        IscrizioniGroupByEvento = Iscrizioni.objects.values('id_evento').annotate(total=Count('id')).filter(id_user = self.request.user.id)
#        print(self.request.user.id)
#        print(event_list)
#        print(IscrizioniGroupByEvento)
        paginator = Paginator(event_list, 25) # Show 25 contacts per page.
        page_number = 10
        page_obj = paginator.get_page(page_number)
        context['page_obj'] =page_obj
        context['paginator'] =paginator
        context['IscrizioniGroupByEvento'] = IscrizioniGroupByEvento
        return context
#


@login_required
def creaIscrizione(request,pk):
    evento = get_object_or_404(Eventi,pk=pk)
    if request.method == "POST":
        form = IscrizioneModelForm(request.POST)
        if form.is_valid():
            iscrizione = form.save(commit=False)
            iscrizione.id_evento = evento
            iscrizione.id_user = request.user
            iscrizione.save()
            success_url = reverse_lazy('lista_eventi')
            success_url = reverse_lazy('user_iscrizioni_list',kwargs={'pk':evento.id})
            success_url = reverse_lazy('user_iscrizioni_list_for_evento',kwargs={'pk':evento.id})
            return HttpResponseRedirect(success_url)
#            return HttpResponseRedirect('/')

    else:
        form = IscrizioneModelForm()
        lista_nominativi = AnagraficaNominativi.objects.all()
        context = {'form':form, 'evento':evento,'lista_nominativi':lista_nominativi}
        return render(request,"iscrizione/crea_iscrizione_new.html",context)


@login_required
def creaEvento(request):
    if request.method == "POST":
        form = EventoModelForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.save()
            success_url = reverse_lazy('lista_eventi')
            return HttpResponseRedirect(success_url)


    else:
        form = EventoModelForm()
    context = {'form':form}
    return render(request,"iscrizione/crea_evento.html",context)


@login_required
def creaFermata(request):
    if request.method == "POST":
        form = TabellaFermateModelForm(request.POST)
        if form.is_valid():
            fermata = form.save(commit=False)
            fermata.save()
            success_url = reverse_lazy('lista_eventi')
            return HttpResponseRedirect(success_url)

    else:
        form = TabellaFermateModelForm()
    context = {'form':form}
    return render(request,"iscrizione/crea_fermata.html",context)
