from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from CustomerID.models import Customer  
from CustomerID.views import login_view  

class CustomerViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.customer = Customer.objects.create(name='Test Customer')



class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful login


    