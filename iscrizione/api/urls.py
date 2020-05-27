from django.urls import path
from iscrizione.api.views import (IscrizioniListCreateAPIView,IscrizioniDetailAPIView,
                                EventiListCreateAPIView,EventiDetailAPIView,IscrizioniCreateAPIView,
                                IscrizioniDeleteAPIView,AnagraficaNominativiCreateAPIView,
                                AnagraficaNominativiRUDAPIView,anagraficaNominativiDeleteAll)

urlpatterns = [
    path('iscrizioni/', IscrizioniListCreateAPIView.as_view(),name = 'iscrizione-list'),
    path('iscrizioni/<int:pk>', IscrizioniDetailAPIView.as_view(),name = 'iscrizione-detail'),
    path('iscrizioni/<int:pk>/delete', IscrizioniDeleteAPIView.as_view(),name = 'iscrizione-delete'),
    path('eventi/', EventiListCreateAPIView.as_view(),name = 'eventi-list'),
    path('nominativi/', AnagraficaNominativiCreateAPIView.as_view(),name = 'nominativi'),
    path('nominativi/<int:pk>/', AnagraficaNominativiRUDAPIView.as_view(),name = 'anagraficanominativi-detail'),
    path('nominativi/deleteall/', anagraficaNominativiDeleteAll.as_view(),name = 'nominativi-Delete-All'),

    path('eventi/<int:pk>', EventiDetailAPIView.as_view(),name = 'evento-detail'),
    path('eventi/<int:evento_pk>/iscrizione', IscrizioniCreateAPIView.as_view(),name = 'evento-detail-iscrizione'),

#    path('ebooks/<int:ebook_pk>/review', ReviewCreateAPIView.as_view(),name = 'review-ebook'),
#    path('reviews/<int:pk>', ReviewDetailAPIView.as_view(),name = 'review-detail'),
]
