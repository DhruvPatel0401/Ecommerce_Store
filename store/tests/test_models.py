from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'Django')

    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data = self.data1
        response = self.client.post(reverse('store:category_list', args=[data.slug]))
        print(response)
        self.assertEqual(response.status_code, 200)