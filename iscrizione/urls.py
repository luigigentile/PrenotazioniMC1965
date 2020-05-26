from django.urls import path
from iscrizione.views  import (creaIscrizione,EventList,UserIscrizioniList,creaEvento,creaFermata,
                    UserIscrizioniListForEvento,UpdateIscrizione,CancellaIscrizione)
from iscrizione.views  import creaSimulazione


urlpatterns = [
#    path('nuova-sezione/', views.CreaSezione.as_view(),name='crea_sezione'),
#    path('sezione/<int:pk>/elimina-sezione', views.CancellaSezione.as_view(),name='cancella_sezione'),
#    path('sezione/<int:pk>', views.visualizzaSezione,name='sezione_view'),
#     path('useriscrizionilist', UserIscrizioniList.as_view(),name='user_iscrizioni_list'),
     path('<int:pk>/useriscrizionilistforevento', UserIscrizioniListForEvento.as_view(),name='user_iscrizioni_list_for_evento'),
     path('<int:pk>/update/', UpdateIscrizione.as_view(), name="update_iscrizione"),
     path('<int:pk>/delete/', CancellaIscrizione.as_view(), name="delete_iscrizione"),
     path('evento/<int:pk>/crea_iscrizione', creaIscrizione,name='crea_iscrizione'),
     path('crea_evento', creaEvento,name='crea_evento'),
     path('listaeventi/', EventList.as_view(), name = 'lista_eventi'),
     path('crea_fermata', creaFermata,name='crea_fermata'),
     path('crea_simulazione', creaSimulazione,name='crea_simulazione'),
]
#
