from django.test import TestCase
from .models import Cohort

# Create your tests here.
class CohortTestClass(TestCase):
    #setupmethod 
    def setUp(self):
        self.name = Cohort(name='')

    #test the instance made is correct

    def test_instance(self):
        self.assertTrue(isinstance(self.name, Cohort))

    #testing the save method 
    def test_save_method(self):
        self.name.save_cohort()
        cohorts = Cohort.objects.all()
        self.assertTrue(len(cohorts)> 0)

