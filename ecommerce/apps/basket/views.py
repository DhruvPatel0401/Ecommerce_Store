from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from ecommerce.apps.catalogue.models import Product
from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, "basket/summary.html", {"basket": basket})


"""
This function is called when the user clicks the "add to basket" button on a products single.html page. It retrieves the product ID and quantity 
from the request's POST data, retrieves the corresponding Product object from the database using get_object_or_404, and adds the product to the 
user's basket using the add method of the Basket object. Finally, it returns a JSON response with the updated quantity of items in the basket.
"""


def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({"qty": basketqty})
        return response


"""
The basket_delete() function takes a request object as input, creates a new instance of a Basket object and checks if the request method is a POST 
and if the action is 'post'. If so, it extracts the product ID from the request data, passes it to the delete() method of the Basket object, and 
returns a JSON response containing the updated subtotal and quantity of items in the basket.
"""


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({"subtotal": baskettotal, "qty": basketqty})
        return response


"""
The basket_update() function updates the quantity of a product in the basket using the update() method of the Basket object. It then returns a 
JSON response containing the updated subtotal and quantity of items in the basket.
"""


def basket_update(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({"qty": basketqty, "subtotal": baskettotal})
        return response
