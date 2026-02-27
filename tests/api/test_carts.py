from src.clients.cart_client import CartClient
from src.utils.assertions import assert_status_in, assert_has_keys


def test_get_cart_by_id_success():
    client = CartClient()
    resp = client.get_cart_by_id(1)

    assert_status_in(resp, (200,))
    data = resp.json()
    assert data["id"] == 1
    assert_has_keys(data, ["products"])
    assert isinstance(data["products"], list)


def test_add_to_cart_success():
    client = CartClient()
    resp = client.add_to_cart(
        user_id=1,
        products=[{"id": 1, "quantity": 2}, {"id": 2, "quantity": 1}],
    )

    assert_status_in(resp, (200, 201))
    data = resp.json()
    assert_has_keys(data, ["products"])
    assert any(p.get("id") == 1 for p in data["products"])


def test_add_to_cart_negative_missing_products():
    client = CartClient()
    # Missing products key intentionally
    resp = client.post("/carts/add", json={"userId": 1})

    assert_status_in(resp, (400, 422))