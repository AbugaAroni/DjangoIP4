from django.urls import path, re_path
from . import views

urlpatterns=[
    path('',views.home, name='Welcome'),
    path('accounts/profile/', views.profile, name='user_profile'),   
]
