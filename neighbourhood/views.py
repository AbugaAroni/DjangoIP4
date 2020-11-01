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

    return render(request, 'homepage.html')

@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            newhood = form.save(commit=False)
            newhood.admin = current_user
            newhood.save()
            newhood.update_occupants(newhood.id)
        return redirect(new_neighbourhood)

    else:
        form = NewNeighbourhoodForm()
    return render(request, 'neighbourhood.html', {"form": form})
