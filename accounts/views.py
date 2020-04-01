from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .forms import FormRegistrazione

# Create your views here.
def registrazioneView(request):
    print(request.method)
    if request.method == "POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            print(password)
            User.objects.create_user(username=username,password=password,email=email)
            user = authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect('/')
    else:
        form = FormRegistrazione()
    context = {'form': form}
    return render(request,'accounts/registrazione.html',context)# Create your views here.
