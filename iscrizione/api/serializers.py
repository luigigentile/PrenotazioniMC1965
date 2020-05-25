from rest_framework import serializers
from iscrizione.models import Eventi,TabellaFermate,Iscrizioni,AnagraficaNominativi

class IscrizioniSerializer(serializers.ModelSerializer):

#    id_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Iscrizioni
#        fields ='__all__'
        exclude = ['id_evento','id_user']   #  passato automaticamente via Perform


class EventiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Eventi
        fields ='__all__'


class AnagraficaNominativiSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnagraficaNominativi
        fields ='__all__'
#
