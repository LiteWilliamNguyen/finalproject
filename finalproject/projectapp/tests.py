from django.test import TestCase
from django.urls import reverse
from .models import Medication, Pharmacist, Technician,Shift
from django.contrib.auth.models import User
from .forms import MedicationForm, PharmacistForm, TechnicianForm, ShiftForm
import datetime
# Create your tests here.

class MedicationTest(TestCase):
    def test_string(self):
        type=Medication(medname="Sertraline")
        self.assertEqual(str(type),type.medname)

    def test_table(self):
        self.assertEqual(str(Medication._meta.db_table), 'Medication')

class PharmacistTest(TestCase):
    def test_string(self):
        type=Pharmacist(pharmname="Henry Beckman")
        self.assertEqual(str(type),type.pharmname)

    def test_table(self):
        self.assertEqual(str(Pharmacist._meta.db_table), 'Pharmacist')

class TechnicianTest(TestCase):
    def test_string(self):
        type=Technician(techname="Bob Rylan")
        self.assertEqual(str(type),type.techname)

    def test_table(self):
        self.assertEqual(str(Technician._meta.db_table), 'Technician')


class Pharmacist_Form_Test(TestCase):
    def setUp(self):
        self.user=User.objects.create(username="user1", password="P@ssw0rd1")
        self.pharmname=Pharmacist.objects.create(pharmname='title1')
    

class Medication_Form_Test(TestCase):
    def setUp(self):
        self.user=User.objects.create(username="user1", password="P@ssw0rd1")

    def test_MedicationForm(self):
        data={
            'medname': 'name1',
            'meddescription': 'some type',
            'medusage': 'some usage',
            'medwarning': 'some warning',
            'medquantity': int,
            'user': self.user,
            'medcost' : int
        }
        form=MedicationForm(data=data)
        self.assertTrue(form.is_valid)

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetMedicationTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.med=Medication.objects.create(medname='Sertraline',
        meddescription='some description',
        medusage='some usage',
        medwarning='some warning',
        medquantity=200,
        user=self.u,
        medcost=200)
        

    
        