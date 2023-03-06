from django.shortcuts import render, get_object_or_404

from .models import Category, Product

"""
The categories function returns a dictionary containing all the categories, which can be used in templates to display a list of all categories 
available. It is made accessible to all templates by settings.py code 'store.views.categories'
"""
def categories(request):
    return {
        'categories': Category.objects.all()
    }

"""
The all_products function retrieves all the products from the database using the Product model and renders them in the home.html template, 
which is then returned as an HTTP response.
"""
def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})    

"""
The product_details function takes a slug parameter in the URL and uses it to retrieve the corresponding product from the database using the 
get_object_or_404 function. If the product exists and is in stock, the function renders the detail.html template with the product details.
"""
def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)  # If you want to retrieve a single object based on a specific filter parameter and you want to raise a HTTP 404 exception if the object does not exist, you should use get_object_or_404. If you want to handle the DoesNotExist exception yourself, you should use Product.objects.get(slug=slug)
    return render(request, 'store/products/detail.html', {'product': product})

"""
The category_list function takes a category_slug parameter in the URL and uses it to retrieve the corresponding category from the database using 
the get_object_or_404 function. The function then retrieves all the products in the given category using the Product.objects.filter method and 
renders them in the category.html template, along with the category details.
"""
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})