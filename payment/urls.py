from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.BasketView, name='basket'),
    path('orderplaced/', views.order_placed, name='orderplaced'),
    path('webhook/', views.razorpay_webhook),
]