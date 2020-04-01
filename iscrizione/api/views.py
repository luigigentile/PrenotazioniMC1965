from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from iscrizione.models import Eventi,TabellaFermate,Iscrizioni
from iscrizione.api.serializers import EventiSerializer,IscrizioniSerializer
#from ebooks.api.permissions import IsAdminUserOrReadOnly,IsReviewAuthorOrReadOnly
#from ebooks.api.pagination import SmallSetPagination
#
class IscrizioniDeleteAPIView(generics.DestroyAPIView):
    queryset = Iscrizioni.objects.all()
    serilizer_class = IscrizioniSerializer


class IscrizioniListCreateAPIView(generics.ListCreateAPIView):
#class IscrizioniListCreateAPIView(generics.ListAPIView):
    queryset = Iscrizioni.objects.all().order_by('-id')
    serializer_class = IscrizioniSerializer
#    permission_classes = [IsAdminUserOrReadOnly]
#    pagination_class = SmallSetPagination


class IscrizioniDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Iscrizioni.objects.all()
    serializer_class = IscrizioniSerializer
#    permission_classes = [IsAdminUserOrReadOnly]


class EventiListCreateAPIView(generics.ListCreateAPIView):
    queryset = Eventi.objects.all().order_by('-id')
    serializer_class = EventiSerializer
#    permission_classes = [IsAdminUserOrReadOnly]
#    pagination_class = SmallSetPagination


class EventiDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eventi.objects.all()
    serializer_class = EventiSerializer
#    permission_classes = [IsAdminUserOrReadOnly]

class IscrizioniCreateAPIView(generics.CreateAPIView):
    queryset = Iscrizioni.objects.all()
    serializer_class = IscrizioniSerializer
#    permission_classes = [IsReviewAuthorOrReadOnly]
#
    def perform_create(self, serializer):
        evento_pk = self.kwargs.get("evento_pk")
        #for key, value in self.kwargs.items():
        #    print(key,value)
        #print(ebook_pk)
        evento = get_object_or_404(Eventi,pk=evento_pk)
        id_user = self.request.user
#        review_queryset = Review.objects.filter(evento=evento,review_author=review_author)
#        if review_queryset.exists():
#            raise ValidationError("Hai già recensito questo libro")
#
        serializer.save(id_evento=evento,id_user=id_user)




#class IscrizioniListCreate(mixins.ListModelMixin,
#                                      mixins.CreateModelMixin,
#                                      generics.GenericAPIView):
#      queryset = Iscrizioni.objects.all()
#      serializer_class = IscrizioniSerializer
#
#      def get(self,request,*args,**kwargs):
#          return self.list(request,*args,**kwargs)
#
#      def post(self,request,*args,**kwargs):
#          return self.create(request,*args,**kwargs)








#

#

#

#
#class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#        queryset = Review.objects.all()
#        serializer_class = ReviewSerializer
#        permission_classes = [IsReviewAuthorOrReadOnly]
#
#
