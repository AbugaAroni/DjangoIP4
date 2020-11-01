from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=20)
    location  = models.CharField(max_length=50)
    No_occupants = models.IntegerField(default=0)
    admin = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_Neighbourhood(self):
        self.save()

    def delete_Neighbourhood(self):
        self.delete()
