from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import neighbourhood, user, business, post
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import NewUserForm, NewNeighbourhoodForm, NewBusinessForm

# Create your views here.
def home(request):
    posts = "x"
    return render(request, 'homepage.html', {"posts":posts})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user=request.user
    neighbourhoods_avail = neighbourhood.objects.all()

    try:
        actual_user = user.objects.get(name=current_user)
    except user.DoesNotExist:
        actual_user = ""
    if actual_user == "":
        userposts = ""
    else:
        try:
            userposts = post.objects.filter(Q(user_name=actual_user))
        except post.DoesNotExist:
            userposts = ""

    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            newuserprofile = form.save(commit=False)
            newuserprofile.name = current_user
            newuserprofile.save()
        return redirect(profile)

    else:
        form = NewUserForm()
    return render(request, 'accounts/profile.html', {"form": form, "userposts":userposts,  "actual_user":actual_user, "neighbourhoods_avail":neighbourhoods_avail})

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
        return redirect(profile)

    else:
        form = NewNeighbourhoodForm()
    return render(request, 'new_neighbourhood.html', {"form": form})

#add a new business
@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user=request.user
    neighbourhoods_avail = neighbourhood.objects.all()

    try:
        actual_user = user.objects.get(name=current_user)
    except user.DoesNotExist:
        actual_user = ""

    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            newhood = form.save(commit=False)
            newhood.user_owner = actual_user
            newhood.save()
        #redirect to the specific neighbourhood businesses    
        return redirect(new_business)

    else:
        form = NewBusinessForm()
    return render(request, 'new_business.html', {"form": form, "actual_user": actual_user, "neighbourhoods_avail":neighbourhoods_avail})
