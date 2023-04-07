from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

import razorpay

from basket.basket import Basket

@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.','')
    razoramount = int(total) + 50
    userid = request.user.id
    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    data = {"amount": razoramount, "currency": "INR", "receipt": "order_rcptid_11"}
    payment_response = client.order.create(data=data)
    print(userid)
    print(client)
    print(payment_response)

    return render(request, "payment/home.html", locals())
