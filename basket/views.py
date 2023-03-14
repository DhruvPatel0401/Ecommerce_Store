from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from store.models import Product
from .basket import Basket

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})


"""
This function is called when the user clicks the "add to basket" button on a products single.html page. It retrieves the product ID and quantity 
from the request's POST data, retrieves the corresponding Product object from the database using get_object_or_404, and adds the product to the 
user's basket using the add method of the Basket object. Finally, it returns a JSON response with the updated quantity of items in the basket.
"""
def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        response = JsonResponse({'Success': True})
        return response