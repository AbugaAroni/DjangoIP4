from django.test import TestCase
from models import neighborhood
from django.db import models
from django.contrib.auth.models import User
# Create your tests here.
class NeighborhoodTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abuga = User(username="rick", password="password")
        self.abuga.save()
        self.neighbourhood= Neighbourhood(name = "MC31", location= "langata", no_occupants = 1, admin = self.abuga)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,neighbourhood))

    # Testing Save Method
    def test_save_method(self):
        self.neighbourhood.save_Neighbourhood()
        testsaved = neighbourhood.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.neighbourhood.save_Neighbourhood()
        testsaved = neighbourhood.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.neighbourhood.delete_Neighbourhood()
        testdelete = neighbourhood.objects.filter(name="MC31")
        self.assertEqual(len(testdelete), 0)
