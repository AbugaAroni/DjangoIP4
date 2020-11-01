from django.test import TestCase
from django.db import models
from .models import neighbourhood, user, business, post
from django.contrib.auth.models import User
# Create your tests here.
class NeighborhoodTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abuga = User(username="rick", password="password")
        self.abuga.save()
        self.neighbourhood= neighbourhood(name = "MC31", location= "langata", no_occupants = 1, admin = self.abuga)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,neighbourhood))

    # Testing Save Method
    def test_save_method(self):
        self.neighbourhood.save_neighbourhood()
        testsaved = neighbourhood.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.neighbourhood.save_neighbourhood()
        testsaved = neighbourhood.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.neighbourhood.delete_neighbourhood()
        testdelete = neighbourhood.objects.filter(name="MC31")
        self.assertEqual(len(testdelete), 0)

    # Testing find Method
    def test_find_method(self):
        self.neighbourhood.save_neighbourhood()
        testsaved = neighbourhood.objects.all()
        self.assertTrue(len(testsaved) > 0)

        findtest = neighbourhood.find_neighbourhood(self.neighbourhood.id)
        self.assertEqual(findtest, self.neighbourhood)

    #testing occupation update Method
        self.neighbourhood.save_neighbourhood()
        testsaved = neighbourhood.objects.all()
        self.assertTrue(len(testsaved) > 0)

        updatetest = neighbourhood.update_occupants(self.neighbourhood.id)
        self.assertEqual(1,self.neighbourhood.no_occupants)

    #testing neighbourhood update Method
        self.neighbourhood.save_neighbourhood()
        testsaved = neighbourhood.objects.all()
        self.assertTrue(len(testsaved) > 0)

        nhood_test = self.neighbourhood
        self.neighbourhood.update_neighborhood()
        self.assertEqual(nhood_test,self.neighbourhood)

class userTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abuga = User(username="rick", password="password")
        self.abuga.save()
        self.neighbourhood= neighbourhood(name = "MC31", location= "langata", no_occupants = 1, admin = self.abuga)
        self.neighbourhood.save()

        self.abugauser = user(name = self.abuga, national_id=33333333, nhood = self.neighbourhood)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugauser,user))

    # Testing Save Method
    def test_save_method(self):
        self.abugauser.save_user()
        testsaved = user.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.abugauser.save_user()
        testsaved = user.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.abugauser.delete_user()
        testdelete = user.objects.filter(name=self.abuga)
        self.assertEqual(len(testdelete), 0)

class BusinessTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abuga = User(username="rick", password="password")
        self.abuga.save()
        self.neighbourhoodx= neighbourhood(name = "MC31", location= "langata", no_occupants = 1, admin = self.abuga)
        self.neighbourhoodx.save()
        self.abugauser = user(name = self.abuga, national_id=33333333, nhood = self.neighbourhoodx)
        self.abugauser.save()

        self.abugabusiness = business(name="carrefour",business_email= "carrefour@gmail.com", user_owner = self.abugauser, nhood= self.neighbourhoodx,  emergency_service = True)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugabusiness,business))

    # Testing Save Method
    def test_save_method(self):
        self.abugabusiness.create_business()
        testsaved = business.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.abugabusiness.create_business()
        testsaved = business.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.abugabusiness.delete_business()
        testdelete = business.objects.filter(name="carrefour")
        self.assertEqual(len(testdelete), 0)

    # Testing find Method
    def test_find_method(self):
        self.abugabusiness.create_business()
        testsaved = business.objects.all()
        self.assertTrue(len(testsaved) > 0)

        findtest = business.find_business(self.abugabusiness.id)
        self.assertEqual(findtest, self.abugabusiness)

    #testing occupation update Method
        self.abugabusiness.create_business()
        testsaved = business.objects.all()
        self.assertTrue(len(testsaved) > 0)

        business_test = self.abugabusiness
        self.abugabusiness.update_business()
        self.assertEqual(business_test,self.abugabusiness)

class PostTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abuga = User(username="rick", password="password")
        self.abuga.save()
        self.neighbourhoodx= neighbourhood(name = "MC31", location= "langata", no_occupants = 1, admin = self.abuga)
        self.neighbourhoodx.save()
        self.abugauser = user(name = self.abuga, national_id=33333333, nhood = self.neighbourhoodx)
        self.abugauser.save()

        self.abugapost = post(title="carrefour closing down", user_name= self.abugauser, article= "carrefour@gmail.com is finally closing doown")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugapost,post))

    # Testing Save Method
    def test_save_method(self):
        self.abugapost.save_post()
        testsaved = post.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.abugapost.save_post()
        testsaved = post.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.abugapost.delete_post()
        testdelete = post.objects.filter(title="carrefour closing down")
        self.assertEqual(len(testdelete), 0)
