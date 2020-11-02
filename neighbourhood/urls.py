from django.urls import path, re_path
from . import views

urlpatterns=[
    path('',views.home, name='Welcome'),
    path('accounts/profile/', views.profile, name='user_profile'),
    path('new/neighbourhood', views.new_neighbourhood, name='add_neighbourhood'),
    path('new/business', views.new_business, name='new_business'),
    path('new/post', views.new_post, name='new_post'),
    path('all/businesses/', views.new_post, name='new_post'),
    re_path('all/businesses/neighbourhood/(\d+)',views.all_businesses,name ='all_businesses'),
    re_path('all/emergencyservices/neighbourhood/(\d+)',views.emergency_services, name ='emergency_services'),                     
]
