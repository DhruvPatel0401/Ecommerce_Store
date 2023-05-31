import factory
from ecommerce.apps.account.models import Address, Customer
from ecommerce.apps.catalogue.models import Category, ProductType, ProductSpecification, Product, ProductSpecificationValue
from faker import Faker

fake = Faker()

####
# Catalogue
####

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = "django"
    slug = "django"

class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType
        django_get_or_create = ("name",)

    name = "book"

class ProductSpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecification

    product_type = factory.SubFactory(ProductTypeFactory)
    name = "pages"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    product_type = factory.SubFactory(ProductTypeFactory)
    category = factory.SubFactory(CategoryFactory)
    title = "product_title"
    description = fake.text()
    slug = "product_slug"
    regular_price = "9.99"
    discount_price = "4.99"


class ProductSpecificationValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecificationValue

    product = factory.SubFactory(ProductFactory)
    specification = factory.SubFactory(ProductSpecificationFactory)
    value = "100"

####
# Account
####

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = "admin@gmail.com"
    name = "admin"
    mobile = "07525251252"
    password = "tester"
    is_active = True
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)
