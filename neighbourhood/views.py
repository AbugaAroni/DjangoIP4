from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import neighbourhood, user, business
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import NewUserForm, NewNeighbourhoodForm

# Create your views here.
def home(request):
    posts = "x"
    return render(request, 'homepage.html', {"posts":posts})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user=request.user
    try:
        actual_user = user.objects.get(name=current_user)
    except user.DoesNotExist:
        actual_user = ""
    try:
        userposts = posts.objects.filter(Q(user_name=actual_user))
    except posts.DoesNotExist:
        userposts = ""

    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            newuserprofile = form.save(commit=False)
            newuserprofile.name = current_user
            newuserprofile.save()
        return redirect(profile)

    else:
        form = NewNeighbourhoodForm()
    return render(request, 'accounts/profile.html', {"form": form, "userposts":userposts,  "actual_user":actual_user})

#add a new neighbourhood
@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            newhood = form.save(commit=False)
            newhood.admin = current_user
            newhood.save()
        return redirect(new_neighbourhood)

    else:
        form = NewNeighbourhoodForm()
    return render(request, 'new_neighbourhood.html', {"form": form})
