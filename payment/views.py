from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

import razorpay

from basket.basket import Basket

def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')

@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price() + 50)
    total = total.replace('.','')
    razoramount = int(total) 
    userid = request.user.id
    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    data = {"amount": razoramount, "currency": "INR", "receipt": "order_rcptid_11"}
    payment_response = client.order.create(data=data)
    print(payment_response)
    # {'id': 'order_LatSMquY4zZz3I', 'entity': 'order', 'amount': 109950, 'amount_paid': 0, 'amount_due': 109950, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1680868761}
    order_id = payment_response['id']
    order_status = payment_response['status']
    # if order_status == 'created':
    #     payment = Payment(
    #         user = userid,
    #         amount = razoramount,
    #         razor_order_id = order_id,
    #         razorpay_payment_status = order_status 
    #     )
    #     payment.save()

    return render(request, "payment/home.html", locals())

