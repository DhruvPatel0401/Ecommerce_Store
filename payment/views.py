from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from basket.basket import Basket

@login_required
def BasketView(request):

    basket = Basket(request)
    total = basket.get_total_price()

    return render(request, "payment/home.html", {'total_amount': total})
