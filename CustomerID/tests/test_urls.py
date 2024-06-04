from django.test import TestCase
from django.urls import reverse


class UrlsTestCase(TestCase):
    def test_customer_list_api_url_resolves(self):
        url = reverse('CustomerID:customer-list')
        self.assertEqual(url, '/api4/customers/')

    def test_product_list_url_resolves(self):
        url = reverse('product_list')
        self.assertEqual(url, '/products1/')
