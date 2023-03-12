

"""
A base Basket class, providing some default behaviors that
can be inherited or overrided, as necessary.
"""
class Basket():

    """
    The '__init__' method initializes the shopping basket by getting the session data and setting the 'basket' attribute to the value of the 'skey' 
    key in the session data, or an empty dictionary if the skey key does not exist in the session.
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}

        self.session.modified = True
        
    def __len__(self):
        """
        Get the basket data and count the quantity of items
        """
        return sum(item['qty'] for item in self.basket.values())