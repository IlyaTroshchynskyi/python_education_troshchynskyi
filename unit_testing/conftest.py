# -*- coding: utf-8 -*-
"""
   Collect all fixtures for tests
"""

import pytest
from to_test import Product, Shop


@pytest.fixture(scope="function", name='instance_product')
def init_class_product():
    """
    Create and delete product for tests
    """
    my_product = Product('Samsung s21', 25000, 2)
    yield my_product
    del my_product


@pytest.fixture(scope="function", name='instance_shop')
def init_class_shop(instance_product):
    """
    Create and delete shop for tests
    """
    my_shop = Shop(instance_product)
    yield my_shop
    del my_shop
