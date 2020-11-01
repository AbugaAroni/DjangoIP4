from django.test import TestCase
from django.db import models
from .models import neighbourhood
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
