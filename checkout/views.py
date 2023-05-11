import razorpay
from basket.basket import Basket
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from basket.basket import Basket

from orders.models import Order, OrderItem
from account.models import Address
from .models import DeliveryOptions

@login_required
def deliverychoices(request):
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    return render(request, "checkout/delivery_choices.html", {"deliveryoptions": deliveryoptions})

@login_required
def basket_update_delivery(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        delivery_option = int(request.POST.get("deliveryoption"))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        updated_total_price = basket.basket_update_delivery(delivery_type.delivery_price)

        session = request.session
        if "purchase" not in request.session:
            session["purchase"] = {
                "delivery_id": delivery_type.id,
            }
        else:
            session["purchase"]["delivery_id"] = delivery_type.id
            session.modified = True

        response = JsonResponse({"total": updated_total_price, "delivery_price": delivery_type.delivery_price})
        return response

@login_required
def delivery_address(request):
    session = request.session
    if "purchase" not in request.session:
        messages.success(request, "Please select delivery option")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    addresses = Address.objects.filter(customer=request.user).order_by("-default")

    if "address" not in request.session:
        session["address"] = {"address_id": str(addresses[0].id)}
    else:
        session["address"]["address_id"] = str(addresses[0].id)
        session.modified = True

    return render(request, "checkout/delivery_address.html", {"addresses": addresses})

@login_required
def payment_selection(request):
    session = request.session
    if "address" not in request.session:
        messages.success(request, "Please select address option")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    basket = Basket(request)
    amount = int(basket.get_total_price()*100)
    
    Data = {
        "amount":  amount,
        "currency": "INR",
        "payment_capture": 1
    }
    payment = client.order.create(data=Data)

    print("*****************************")
    print(payment)
    print("*****************************")
    return render(request, "checkout/payment_selection.html", {'payment': payment})

@login_required
def payment_complete(request):

    # order = Order.objects.create(
    #     user_id=user_id,
    #     full_name=response.result.purchase_units[0].shipping.name.full_name,
    #     email=response.result.payer.email_address,
    #     address1=response.result.purchase_units[0].shipping.address.address_line_1,
    #     address2=response.result.purchase_units[0].shipping.address.admin_area_2,
    #     postal_code=response.result.purchase_units[0].shipping.address.postal_code,
    #     country_code=response.result.purchase_units[0].shipping.address.country_code,
    #     total_paid=response.result.purchase_units[0].amount.value,
    #     order_key=response.result.id,
    #     payment_option="paypal",
    #     billing_status=True,
    # )
    # order_id = order.pk

    # print(order)
    
    return JsonResponse("Payment completed!", safe=False)
