from django.shortcuts import render

# Create your views here.
def home(request):
    allprojects = "x"
    return render(request, 'homepage.html', {"projects":allprojects})
