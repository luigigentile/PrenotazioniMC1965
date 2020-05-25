from django.contrib import admin
from iscrizione.models import Eventi,TabellaFermate,Iscrizioni,AnagraficaNominativi
from iscrizione.models import PowerData

## Register your models here.
admin.site.register(Eventi)
admin.site.register(Iscrizioni)
admin.site.register(TabellaFermate)
admin.site.register(AnagraficaNominativi)
admin.site.register(PowerData)
