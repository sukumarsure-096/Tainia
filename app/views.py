from django.shortcuts import render

from django.views.generic import TemplateView,FormView

from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth import authenticate,login,logout

from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError

from app.form import *

from app.models import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    uf = user_form()
    pf = profile_form()
    if request.method=='POST' and request.FILES:
        uf = user_form(request.POST)
        pf = profile_form(request.POST,request.FILES)
        if uf.is_valid() and pf.is_valid():
            user=uf.save(commit=False)
            user.set_password(uf.cleaned_data['password'])
            user.save()
            pro = pf.save(commit=False)
            pro.user_name=user
            pro.save()
            return HttpResponseRedirect(reverse('home'))
            
    d = {'uf':uf,'pf':pf}
    return render(request,'signup.html',context=d)
    
    #return render(request,'signup.html')
    

def Log_in(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        ua = authenticate(username=username,password=password)
        if ua and ua.is_active:
            login(request,ua)
            request.session['username'] = username
            return HttpResponseRedirect(reverse('home'))
        else:
            raise ValidationError('user is not active')
    return render(request,'Login.html')

@login_required
def Log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Log_in'))
'''
@login_required
def profile(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    pro = profile.objects.get(user_name=user)
    d = {'user':user,'pro':pro}
    return render(request,'profile.html',context=d)
'''
@login_required
def profiles(request):
    un = request.session['username']
    user = User.objects.get(username=un)
    pfl = profile.objects.get(user_name=user)
    return render(request,'profile.html',context={'user':user,'profile':pfl})

@login_required
def cp(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    if request.method=='POST':
        pass_word = request.POST['password']
        user.set_password(pass_word)
        user.save()
    return render(request,'cp.html')

def reset(request):
    if request.method == 'POST':
        us = request.POST['username']
        user = User.objects.get(username=us)
        pw = request.POST['password']
        user.set_password(pw)
        user.save()
    return render(request,'reset.html')

class icon(TemplateView):
    template_name='icon.html'    

def tm(request):
     return render(request,'tm.html')


