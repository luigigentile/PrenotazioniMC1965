from django import forms

from .models import Iscrizioni,Eventi,TabellaFermate

class IscrizioneModelForm(forms.ModelForm):
    class Meta:
        model = Iscrizioni
        fields = ['nome','cognome','luogo_di_nascita','data_nascita','telefono','id_fermata']
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Nome"}),
            "cognome": forms.TextInput(attrs={"placeholder": "cognome"}),
            "data_nascita": forms.DateInput(attrs={"placeholder": "data di nascita"})
        }


class EventoModelForm(forms.ModelForm):
    class Meta:
        model = Eventi
        fields = ['evento','nota','parte_da','numero_massimo_iscritti','data_evento']

class TabellaFermateModelForm(forms.ModelForm):
    class Meta:
        model = TabellaFermate
        fields = ['fermata']



#from .models import Discussione,Post
#
#class DiscussioneModelForm(forms.ModelForm):
#    contenuto = forms.CharField(
#        widget=forms.Textarea(attrs={"placeholder": "Di cosa vuoi parlarci?"}),
#        max_length=4000, label = "Primo Messaggio")
#
#    class Meta:
#        model = Discussione
#        fields = ["titolo", "contenuto"]
#        widgets = {
#            "titolo": forms.TextInput(attrs={"placeholder": "Titolo della Discussione"})
#        }
#
#class PostModelForm(forms.ModelForm):
#
#    class Meta:
#        model = Post
#        fields = ["contenuto"]
#        widgets = {
#            "contenuto": forms.Textarea(attrs={"rows": '5'})
#        }
#        labels = {
#            "contenuto": 'Messaggio'
#        }
#
