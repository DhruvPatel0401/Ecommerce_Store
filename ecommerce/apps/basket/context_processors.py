from .basket import Basket

"""
This code defines a context processor called basket that creates a new instance of the Basket class and makes it available as a context variable 
for every template rendered for the request.
"""


def basket(request):
    return {"basket": Basket(request)}
