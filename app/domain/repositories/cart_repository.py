from abc import ABC, abstractmethod

from app.domain.entities.cart import Cart


class CartRepository(ABC):
    @abstractmethod
    def get_current(self) -> Cart:
        pass

    @abstractmethod
    def save(self, cart: Cart):
        pass

