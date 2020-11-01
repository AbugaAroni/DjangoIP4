from django import forms
from .models import neighbourhood, user, business

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
