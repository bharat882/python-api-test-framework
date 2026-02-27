from src.clients.base_client import BaseClient


class ProductsClient(BaseClient):
    def get_product_by_id(self, product_id: int):
        return self.get(f"/products/{product_id}")

    def search_products(self, query: str):
        return self.get("/products/search", params={"q": query})

    def get_all_products(self, limit: int = 10):
        return self.get("/products", params={"limit": limit})