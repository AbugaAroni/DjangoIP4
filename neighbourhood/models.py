from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class neighbourhood(models.Model):
    name = models.CharField(max_length=20)
    location  = models.CharField(max_length=50)
    no_occupants = models.IntegerField(default=0)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls,hoodid):
        hood = cls.objects.get(id = hoodid)
        return hood

    @classmethod
    def update_occupants(cls,hoodid):
        occupationcount = cls.objects.get(id=hoodid)
        newcount = occupationcount.no_occupants + 1
        cls.objects.filter(id = hoodid).update(no_occupants = newcount)

    def update_neighborhood(self):
        name = self.name
        self.name = name
