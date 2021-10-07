# -*- coding: utf-8 -*-
"""
   Collect all tests for project
"""


import pytest
from to_test import even_odd, sum_all, time_of_day, Product


@pytest.mark.parametrize("number, expected_result", [(1, "odd"), (2, "even"),
                                                     (3, "odd"), (-5, "odd"),
                                                     (-6, "even")])
def test_even_odd(number, expected_result):
    """
    Tests func even_odd which return if number even or odd
    """
    assert even_odd(number) == expected_result


@pytest.mark.parametrize("number", list(range(100)))
def test_even_odd_valid_value(number):
    """
    Test func even_odd which return if number even or odd
    """
    assert even_odd(number) in ("even", "odd")


@pytest.mark.parametrize("sum_numbers, expected_result", [([1, 2, 3], 6), ([1], 1),
                                                          ([-1, -3, -5], -9),
                                                          ([-5, 5], 0), ([9.9, 0.1], 10)])
def test_sum_all(sum_numbers, expected_result):
    """
    Tests func sum_all which sums all given numbers together.
    """
    assert sum_all(*sum_numbers) == expected_result


@pytest.mark.xfail(reason="test negative result")
def test_sum_all_negative():
    """
    Tests func sum_all which sums all given numbers together.
    """
    assert sum_all(1, 2) == 4


def test_time_of_day():
    """
    Tests func sum_all which identifies current time of day.
    """
    assert time_of_day() in ("night", "morning", "afternoon", "night")


@pytest.mark.xfail(reason="test negative result")
def test_time_of_day_negative():
    """
    Test func sum_all which identifies current time of day.
    Show the error when func return extra value
    """
    assert time_of_day() not in ("night", "morning", "afternoon", "night")


def test_init_product(instance_product):
    """
    Test representation of a product in a shop after initialization.
    Input fixture.
    """
    assert instance_product.price == 25000
    assert instance_product.quantity == 2
    assert instance_product.title == 'Samsung s21'


def test_subtract_quantity(instance_product):
    """
    Test func subtract the number of available products.
    Input fixture.
    """
    instance_product.subtract_quantity()
    assert instance_product.quantity == 1


def test_subtract_quantity_without_default(instance_product):
    """
    Test func subtract the number of available products without usage default value.
    Input fixture.
    """
    instance_product.subtract_quantity(2)
    assert instance_product.quantity == 0


def test_add_quantity(instance_product):
    """
    Test func adds the number of available products.
    Input fixture.
    """
    instance_product.add_quantity()
    assert instance_product.quantity == 3


def test_add_quantity_without_default(instance_product):
    """
    Test func adds the number of available products without usage default value.
    Input fixture.
    """
    instance_product.add_quantity(2)
    assert instance_product.quantity == 4


def test_change_price(instance_product):
    """
    Test func change price of one product.
    """
    instance_product.change_price(10000)
    assert instance_product.price == 10000


def test_init_shop(instance_shop):
    """
    Test that shop contains certain product
    """
    assert instance_shop.products[0].title == 'Samsung s21'


def test_add_product(instance_shop):
    """
    Test func which add product to the shop
    """
    test_product = Product('Samsung s22', 30000)
    instance_shop.add_product(test_product)
    assert len(instance_shop.products) == 2
    assert instance_shop.products[1].title == 'Samsung s22'


def test_get_product_index(instance_shop):
    """
    Test func which looks for products in the shop
    """
    test_product = Product('Samsung s22', 30000)
    instance_shop.add_product(test_product)
    assert instance_shop._get_product_index('Samsung s22') == 1
    assert instance_shop._get_product_index('Samsung s26') is None


def test_sell_product_one(instance_shop):
    """
    Test func sells product which returns the final money amount to pay
    """
    test_product = Product('Samsung s22', 30000)
    instance_shop.add_product(test_product)
    assert instance_shop.sell_product('Samsung s22') == 30000
    assert len(instance_shop.products) == 1


def test_sell_product_two(instance_shop):
    """
    Test func sells product which returns the final money amount to pay
    """
    test_product = Product('Samsung s22', 30000)
    instance_shop.add_product(test_product)
    assert instance_shop.sell_product('Samsung s21', 2) == 50000
    assert len(instance_shop.products) == 1


def test_sell_product_test_exception(instance_shop):
    """
    Test func sell product which raise ValueError when quantity of product not enough for order.
    """
    with pytest.raises(ValueError) as exc_info:
        instance_shop.sell_product('Samsung s21', 3)
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "Not enough products"
