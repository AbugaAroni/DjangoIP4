from django import forms
from .models import neighbourhood, user, business, post

class NewNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = neighbourhood
        exclude = ['admin', 'no_occupants']

class NewUserForm(forms.ModelForm):
    class Meta:
        model = user
        exclude = ['name']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = business
        exclude = ['user_owner']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = post
        exclude = ['user_name']
