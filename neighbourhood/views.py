from django.shortcuts import render

# Create your views here.
def home(request):
    allprojects = "x"
    return render(request, 'homepage.html', {"projects":allprojects})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user=request.user
    projects = Project.objects.filter(Q(creator=current_user))
    try:
        profiles = Profile.objects.get(username=current_user)
    except Profile.DoesNotExist:
        profiles = ""

    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            Profilez = form.save(commit=False)
            Profilez.username = current_user
            Profilez.save()
        return redirect(profile)

    else:
        form = NewProfileForm()
    return render(request, 'accounts/profile.html', {"form": form, "projects":projects,  "profiles":profiles})
