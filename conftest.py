import pytest
from pytest_factoryboy import register

from tests.factories import CategoryFactory, ProductTypeFactory, ProductFactory, ProductSpecificationValueFactory, ProductSpecificationFactory

register(CategoryFactory)
register(ProductTypeFactory)
register(ProductSpecificationFactory)
register(ProductSpecificationValueFactory)
register(ProductFactory)

@pytest.fixture
def product_category(db, category_factory):
    category = category_factory.create()
    return category

@pytest.fixture
def product_type(db, product_type_factory):
    product_type = product_type_factory.create()
    return product_type

@pytest.fixture
def product_specification(db, product_specification_factory):
    product_spec = product_specification_factory.create()
    return product_spec


@pytest.fixture
def product(db, product_factory):
    product = product_factory.create()
    return product


@pytest.fixture
def product_spec_value(db, product_specification_value_factory):
    product_spec_value = product_specification_value_factory.create()
    return product_spec_value

