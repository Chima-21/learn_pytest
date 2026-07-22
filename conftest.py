import pytest


@pytest.fixture(scope="module")
def some_calc():
    """Just playing"""
    x = 4
    return x ^ 3


@pytest.fixture(scope="module")
def some_exp():
    """Just played"""
    x = 2
    return x ^ 3
