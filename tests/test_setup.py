from src.clients.base_client import BaseClient


def test_base_url():
    client = BaseClient()
    response = client.get("/products/1")
    assert response.status_code == 200