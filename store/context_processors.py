from .models import Category

"""
The categories function returns a dictionary containing all the categories, which can be used in templates to display a list of all categories 
available. It is made accessible to all templates by settings.py code 'store.context_processors.categories'
"""


def categories(request):
    return {"categories": Category.objects.filter(level=0)}
