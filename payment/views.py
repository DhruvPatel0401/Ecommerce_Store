from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import razorpay

from basket.basket import Basket
from account.models import UserBase
from orders.views import payment_confirmation


def order_placed(request, order_id):
    basket = Basket(request)
    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

    order_key = client.order.fetch(order_id=order_id)
    status = order_key.get('status')

    if status == 'paid':
        payment_confirmation(order_id)
    
    basket.clear()
    return render(request, 'payment/orderplaced.html')

@login_required
def BasketView(request):
    basket = Basket(request)

    total = basket.get_total_price() * 100
    razoramount = int(total) 

    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    data = {"amount": razoramount, "currency": "INR", "receipt": "order_rcptid_11"}
    payment_response = client.order.create(data=data)
    # {'id': 'order_LatSMquY4zZz3I', 'entity': 'order', 'amount': 109950, 'amount_paid': 0, 'amount_due': 109950, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1680868761}
    order_id = payment_response['id']
    order_status = payment_response['status']
    context = {
        'razoramount': razoramount,
        'order_id': order_id,
        'order_status': order_status,
        'email': request.user.email
    }

    return render(request, "payment/home.html", {'context': context})

@csrf_exempt
def razorpay_webhook(request):
    payload = request.body
    event = None
    print("Payload: ",payload)
    
    return HttpResponse(payload, status=200)
