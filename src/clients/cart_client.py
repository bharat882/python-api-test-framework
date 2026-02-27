from src.clients.base_client import BaseClient


class CartClient(BaseClient):
    def get_cart_by_id(self, cart_id: int):
        return self.get(f"/carts/{cart_id}")

    def add_to_cart(self, user_id: int, products: list[dict]):
        """
        products example:
        [{"id": 1, "quantity": 2}, {"id": 2, "quantity": 1}]
        """
        payload = {"userId": user_id, "products": products}
        return self.post("/carts/add", json=payload)