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
        self.assertEqual(response.status_code, 200)
    
class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='Django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=6, title='Django Beginner', created_by_id=1, slug='django-beginner', price='10.99', image='images/default.png')
        self.data2 = Product.product.create(category_id=4, title='Deep Learning', created_by_id=1, slug='deep-learning', price='50.99', image='images/Deep_Learning.jpg', is_active=False)
        
    def test_product_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1 
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Django Beginner')

    def test_products_url(self):
        """
        Test product model slug and URL reverse
        """
        data = self.data1
        url = reverse('store:product_detail', args=[data.slug])
        self.assertEqual(url, '/django-beginners')
        response = self.client.post(
            reverse('store:product_detail', args=[data.slug]))
        self.assertEqual(response.status_code, 200)