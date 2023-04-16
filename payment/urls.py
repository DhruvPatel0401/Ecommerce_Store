from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.BasketView, name='basket'),
    path('orderplaced/<str:order_id>/', views.order_placed, name='orderplaced'),
    path('webhook/', views.razorpay_webhook),
]