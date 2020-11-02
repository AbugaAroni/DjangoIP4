from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

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

class user(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    national_id = models.CharField(max_length=20)
    nhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

class business(models.Model):
    name = models.CharField(max_length=20)
    user_owner = models.ForeignKey(user,on_delete=models.CASCADE)
    nhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    business_email = models.EmailField(max_length=254)
    emergency_service = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,busid):
        biz = cls.objects.get(id = busid)
        return biz

    @classmethod
    def search_by_title(cls,search_term, id):
        img = cls.objects.filter(Q(name__icontains=search_term, nhood=id))
        return img

    def update_business(self):
        name = self.name
        self.name = name

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    article = models.TextField()
    user_name = models.ForeignKey(user,on_delete=models.CASCADE)
    nhoodz = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
