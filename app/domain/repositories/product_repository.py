from abc import ABC, abstractmethod

from app.domain.entities.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def save(self, product: Product):
        pass
