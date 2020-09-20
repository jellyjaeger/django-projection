from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UserRegisteredform,UserUpdateform,ProfileUpdateform
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from . import signals
def registration(request):
    if request.method == 'POST':
        user = UserRegisteredform(request.POST)
        if user.is_valid():
            user.save()
            username=user.cleaned_data.get('username')
            messages.success(request,'Registration for {username} is succesfull '.format(username=username))
            return redirect('login')
    else:
         user = UserRegisteredform()
    return render(request,'registration/formold.html',{
        "users":user
        
    })
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateform(request.POST,instance=request.user)
        p_form = ProfileUpdateform(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request,f'Profile Updated')
            return redirect('profile')
    else:      
        u_form = UserUpdateform(instance=request.user)
        p_form = ProfileUpdateform(instance=request.user.profile)
    return render(request,'registration/profile.html',
    {'u_form': u_form,
    'p_form': p_form})   

         

# Create your views here.
