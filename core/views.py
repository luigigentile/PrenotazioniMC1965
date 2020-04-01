from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.views import logout_then_login
from iscrizioneevento import settings


from iscrizione.models import Iscrizioni
# Create your views here.
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
#    return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
#    print("STATICFILES_DIRS",settings.STATICFILES_DIRS)
    return redirect('%s' % (settings.LOGIN_URL))

#    return render(request,'core/homepage.html')

def homepage(request):
#    return logout_then_login(request,login_url='/login')
    #return logout_then_login(request,login_url='/')
    return render(request,'core/homepage.html')


#def userProfileView(request,username):
#    user = get_object_or_404(User,username=username)
#    discussione_utente = Discussione.objects.filter(autore_discussione = user).order_by('-pk')
#    context = {'user' : user,'discussione_utente':discussione_utente}
#    return render(request,'core/user_profile.html',context)
def userProfileView(request,username):
    user = get_object_or_404(User,username=username)
    iscrizioni_utente = Iscrizioni.objects.filter(id_user = user).order_by('-pk')
    context = {'user' : user,'iscrizioni_utente':iscrizioni_utente}
    return render(request,'core/user_profile.html',context)

class UserList(ListView,LoginRequiredMixin):
    model = User
    paginate_by =3
    template_name = 'core/users.html'
