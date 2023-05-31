import pytest


def test_customer_str(customer):
    assert customer.__str__() == "admin"

def test_customer_str(adminuser):
    assert adminuser.__str__() == "admin_user"

def test_customer_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="")
    assert str(e.value) == "You must provide an email address"