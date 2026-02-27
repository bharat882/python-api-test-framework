import pytest
from src.clients.products_client import ProductsClient
from src.clients.cart_client import CartClient


@pytest.fixture(scope="session")
def products_client():
    return ProductsClient()


@pytest.fixture(scope="session")
def cart_client():
    return CartClient()