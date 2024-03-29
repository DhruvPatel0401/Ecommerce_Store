from ecommerce.apps.catalogue.models import Product
from ecommerce.apps.checkout.models import DeliveryOptions
from decimal import Decimal
from django.conf import settings


"""
A base Basket class, providing some default behaviors that
can be inherited or overrided, as necessary.
"""


class Basket:
    def __init__(self, request):
        """
        The '__init__' method initializes the shopping basket by getting the session data and setting the 'basket' attribute to the value of the
        'skey' key in the session data, or an empty dictionary if the skey key does not exist in the session.
        """
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]["qty"] = qty
        else:
            self.basket[product_id] = {"price": str(product.regular_price), "qty": qty}

        self.save()

    def __iter__(self):
        """
        The method allows the class instance to be iterated over using a for loop, and it returns a generator object that yields a dictionary
        for each item in the basket.
        """
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)

        if product_id in self.basket:
            self.basket[product_id]["qty"] = qty
        self.save()

    def __len__(self):
        """
        Get the basket data and count the quantity of items
        """
        return sum(item["qty"] for item in self.basket.values())

    def get_subtotal_price(self):
        return sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

    def get_delivery_price(self):
        newprice = 0.00

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price
        return newprice

    def get_total_price(self):
        newprice = 0.00
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price
        else:
            newprice = 50
            
        total = subtotal + Decimal(newprice)

        return total

    # def basket_update_delivery(self, deliveryprice=0):
    #     sub_total = sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())
    #     total = sub_total + Decimal(deliveryprice)
    #     return total
        
    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear(self):
        # Remove basket from session
        del self.session[settings.BASKET_SESSION_ID]
        del self.session["address"]
        del self.session["purchase"]
        self.save()

    def save(self):
        self.session.modified = True
