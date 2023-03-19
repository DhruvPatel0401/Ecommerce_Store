from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(id=1, username='admin')
        Category.objects.create(id=1, name='django', slug='django')
        Product.objects.create(id=1, category_id=1, title='django begineers', created_by_id=1, slug='django-beginners', price='20.00', image='django')
        Product.objects.create(id=2, category_id=1, title='django intermediate', created_by_id=1, slug='django-intermediate', price='40.00', image='django')
        Product.objects.create(id=3, category_id=1, title='django advance', created_by_id=1, slug='django-advance', price='80.00', image='django')
        self.client.post(reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        self.client.post(reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)

    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Test adding items to the basket
        """
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        """
        Test deleting items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_delete'), {"productid": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'subtotal': '20.00', 'qty': 1})

    def test_basket_update(self):
        """
        Test updating items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '60.00'})