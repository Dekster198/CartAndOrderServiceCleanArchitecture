from app.domain.entities.cart import CartItem, Cart
from app.domain.repositories.cart_repository import CartRepository


class InMemoryCartRepository(CartRepository):
    def __init__(self):
        self._cart = Cart()

    def get_current(self) -> Cart:
        return self._cart

    def save(self, cart: Cart):
        self._cart = cart
