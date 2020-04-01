from django.http import HttpResponseRedirect,HttpResponseBadRequest
from django.urls import reverse,reverse_lazy
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator # ,EmptyPage,PageNotAnInteger
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import resolve

from django.core.paginator import Paginator
import datetime

# Create your views here.
from .forms import IscrizioneModelForm,EventoModelForm,TabellaFermateModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from iscrizione.models import Eventi,TabellaFermate,Iscrizioni

from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView

# Create your views here.
class CancellaIscrizione(DeleteView):
    model = Iscrizioni
    success_url="/"
    success_url = reverse_lazy('user_iscrizioni_list')
    #success_url = reverse_lazy('visualizza_discussione')
    #success_url = reverse_lazy('visualizza_discussione',kwargs={'pk':post.discussione__id})
    template_name = "iscrizione/iscrizione_confirm_delete.html"
    context_object_name = 'iscrizione_da_eliminare'


class UpdateIscrizione(UpdateView):
    model = Iscrizioni
    fields = ['nome','cognome','telefono','id_fermata']
    template_name = "iscrizione/update_iscrizione.html"
    success_url = reverse_lazy('user_iscrizioni_list')


    def get_context_data(self, **kwargs):
            # Call the base implementation first to get the context
            context = super().get_context_data(**kwargs)
            # Create any data and add it to the context
            context['iscrizioni'] = Iscrizioni.objects.all()
            return context


class UserIscrizioniListForEvento(ListView,LoginRequiredMixin):
    model = Iscrizioni
#    paginate_by =10
    template_name = 'iscrizione/UserIscrizioniList.html'
    context_object_name = 'useriscrizioni'

    def get_queryset(self,*args,**kwargs):
        user_id=self.request.user.id
        evento=self.kwargs.get("pk")
        qset= Iscrizioni.objects.filter(id_user=user_id,id_evento=evento)
        return qset


    def get_context_data(self, **kwargs):
            # Call the base implementation first to get the context
            context = super().get_context_data(**kwargs)
            # Create any data and add it to the context
            context['eventi'] = Eventi.objects.all()
            return context


class UserIscrizioniList(ListView,LoginRequiredMixin):
    model = Iscrizioni
    paginate_by =5
    template_name = 'iscrizione/UserIscrizioniList.html'
    context_object_name = 'useriscrizioni'

    def get_queryset(self,*args):
        user_id=self.request.user.id
        qsuseriscrizioni= Iscrizioni.objects.filter(id_user=user_id).order_by('-id_evento_id')
        print("UserIscrizioniList")
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
        paginator = Paginator(event_list, 25) # Show 25 contacts per page.
        page_number = 10
        page_obj = paginator.get_page(page_number)
        context['page_obj'] =page_obj
        context['paginator'] =paginator
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
            return HttpResponseRedirect(success_url)
#            return HttpResponseRedirect('/')

    else:
        form = IscrizioneModelForm()
    context = {'form':form, 'evento':evento}
    return render(request,"iscrizione/crea_iscrizione.html",context)


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
