from app.domain.entities.product import Product
from app.domain.repositories.product_repository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    def __init__(self, products: list[Product] | None = None):
        self._products: dict[int, Product] = {}

        if products:
            for product in products:
                self._products[product.id] = product

    def get_by_id(self, product_id: int) -> Product:
        try:
            return self._products[product_id]
        except KeyError:
            raise ValueError(f'Product with id={product_id} not found')

    def save(self, product: Product):
        self._products[product.id] = product
