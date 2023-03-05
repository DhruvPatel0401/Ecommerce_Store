from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    #get_aboslute_url is called in template for dynamic linking. Return for generating the URL of the category_list view.
    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])
    
    # for displaying the name of the category in the admin panel.
    def __str__(self):
        return self.name
    

class Product(models.Model):
    """
    The related_name attribute of the category and created_by fields is used to create a reverse relationship between the Product and 
    Category/User models, respectively.
    """
    category = models.ForeignKey(Category,related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creater', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Anonymous')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)  #Ordering is used for default ordering for objects of particular model. 

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    

    def __str__(self):
        return self.title
    