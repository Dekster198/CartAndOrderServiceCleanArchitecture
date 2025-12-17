from dataclasses import dataclass

from app.domain.entities.order import Order


@dataclass
class CreateOrderOutput:
    order_id: int
    total_price: float
    status: str


class CreateOrderUseCase:
    def __init__(self, cart_repo: CartRepository, order_repo: OrderRepository):
        self.cart_repo = cart_repo
        self.order_repo = order_repo

    def execute(self) -> CreateOrderOutput:
        cart = self.cart_repo.get_current()

        if cart.is_empty():
            raise ValueError('Cannot create order from empty cart')

        order = Order.create_from_cart(self.order_repo.next_id(), cart)

        self.order_repo.save(order)
        cart.clear()
        self.cart_repo.save(cart)

        return CreateOrderOutput(
            order_id=order.id,
            total_price=order.total_price,
            status=order.status.value
        )
