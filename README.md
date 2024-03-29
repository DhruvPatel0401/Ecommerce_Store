
# Django based Ecommerce Store

Here's a breakdown of the key features and components of our website:

1. Apps:
Account: This app handles customer-related functionalities such as registration, login, logout, profile management, addresses, orders, and wishlists.<br>
Basket: The Basket app manages the shopping basket, allowing users to add, update, and remove items, view the summary, and calculate prices.<br>Catalogue: This app handles the product catalog, including categories, product types, specifications, images, and detailed product information.<br>
Checkout: The Checkout app manages the payment and delivery process, providing options for payment selections and delivery methods.<br>
Orders: This app handles order placement and management.

2. Account App:
The Account app includes models for storing customer details and a custom account manager. It provides routes for various account-related actions like login, registration, password reset, profile editing, address management, order history, and wishlist functionality. The tokens.py file is responsible for token generation.

3. Basket App:
The Basket app includes a Basket class that manages the user's shopping basket. It provides functions to add, update, and delete items, calculate subtotal and total prices, and retrieve the basket's content. The routes allow users to view the basket summary and perform actions like adding, deleting, and updating items.

4. Catalogue App:
The Catalogue app manages the product catalog. It includes models for categories, product types, specifications, product information, and images. The routes enable users to browse the store, view product details, and explore different categories.

5. Checkout App:
The Checkout app handles the checkout process. It includes models for payment selections and delivery options. The routes allow users to choose delivery options, update delivery details, select payment methods, and complete the payment.

6. Orders App:
The Orders app is responsible for managing orders and order items. It includes a model for storing order information. The routes facilitate the addition of orders.

Other Project Details:

The project utilizes a Postgres database for data storage.
We have integrated Razorpay as our payment gateway for secure and convenient online payments.
All the website templates are located in the "template" folder, while the "static" folder contains CSS and JavaScript files for styling and interactivity.


## Deployment

To deploy this project install python3 and run below commands in terminal

```python
  pip install -r requirements.txt
```

Create .env file and add below details.

DATABASE_URL = postgres://postgres:<password>@localhost:5432/<Database_Name>
RAZOR_KEY_ID = <Your_Razorpay_ID>
RAZOR_KEY_SECRET = <Your_Razorpay_Secret>

```python
py manage.py makemigrations
``` 
```python
py manage.py migrate
``` 
```python
py manage.py createsuperuser
``` 




## Feedback

If you have any feedback, please reach out to us at pateldhruv130401@gmail.com

