from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import neighbourhood, user, business, post
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import NewUserForm, NewNeighbourhoodForm, NewBusinessForm, NewPostForm, ChangeNeighbourhoodForm

# Create your views here.
def home(request):
    current_user=request.user
    if request.user.is_anonymous:
        neighhood = ""
        posts = ""
    else:
        try:
            actual_user = user.objects.get(name=current_user)
        except user.DoesNotExist:
            actual_user = ""
        if actual_user == "":
            neighhood = ""
            posts = ""
        else:
            try:
                neighhood = neighbourhood.objects.get(id=actual_user.nhood.id)
                posts = post.objects.filter(Q(nhoodz=neighhood))
            except post.DoesNotExist:
                neighhood = post.objects.filter(Q(user_name=actual_user))
                posts = ""
    return render(request, 'homepage.html', {"posts":posts, "neighbourhood":neighhood, "posts": posts})

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
            neighbourhood.update_occupants(newuserprofile.nhood.id)
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
        return redirect(all_neighbourhoods)

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
        #redirect to the specific neighbourhood
        return HttpResponseRedirect(reverse("single_neighbourhood", args=[newhood.nhood.id]))

    else:
        form = NewBusinessForm()
    return render(request, 'new_business.html', {"form": form, "actual_user": actual_user, "neighbourhoods_avail":neighbourhoods_avail})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user=request.user
    neighbourhoods_avail = neighbourhood.objects.all()

    try:
        actual_user = user.objects.get(name=current_user)
    except user.DoesNotExist:
        actual_user = ""

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            newhood = form.save(commit=False)
            newhood.user_name = actual_user
            newhood.save()
        #redirect to the neighrboud hood post
        return HttpResponseRedirect(reverse("single_neighbourhood", args=[newhood.nhoodz.id]))

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form, "actual_user": actual_user, "neighbourhoods_avail":neighbourhoods_avail})

def all_businesses(request, nhood_id):
    neighhood = neighbourhood.objects.get(id = nhood_id)
    try:
        biz = business.objects.filter(Q(nhood = neighhood))
    except business.DoesNotExist:
        biz = ""
    return render(request, 'all_businesses.html', {"biz":biz, "neighbourhood":neighhood})


def emergency_services(request, nhood_id):
    neighhood = neighbourhood.objects.get(id = nhood_id)
    try:
        biz = business.objects.filter(Q(nhood = neighhood))
    except business.DoesNotExist:
        biz = ""
    return render(request, 'emergency_services.html', {"biz":biz, "neighbourhood":neighhood})

def single_neighbourhood(request, nhood_id):
    neighhood = neighbourhood.objects.get(id = nhood_id)
    try:
        posts = post.objects.filter(Q(nhoodz=neighhood))
    except post.DoesNotExist:
        posts = ""
    return render(request, 'single_neighbourhood.html', {"posts":posts, "neighbourhood":neighhood})

def all_neighbourhoods(request):
    neighhood = neighbourhood.objects.all()
    return render(request, 'view_allneighbourhoods.html', {"neighbourhood":neighhood})

@login_required(login_url='/accounts/login/')
def search_results(request):
    neighhood = neighbourhood.objects.all()

    if 'business_search' in request.GET and request.GET["business_search"]:
        search_term = request.GET.get("business_search")
        nhoodid = request.GET.get("neighbourhood")
        searched_businesses = business.search_by_title(search_term, nhoodid)
        message = f"{search_term}"

        return render(request, 'searchresult.html',{"message":message,"biz": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searchresult.html',{"message":message})

#add a new neighbourhood
@login_required(login_url='/accounts/login/')
def change_neighbourhood(request):
    current_user=request.user
    try:
        actual_user = user.objects.get(name=current_user)
    except user.DoesNotExist:
        actual_user = ""
    if request.method == 'POST':
        form = ChangeNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            newhood = form.save(commit=False)
            actual_user.change_hood(actual_user.id, newhood.nhood)
        return redirect(profile)

    else:
        form = ChangeNeighbourhoodForm()
    return render(request, 'change_neighbourhood.html', {"form": form, "user": actual_user})
