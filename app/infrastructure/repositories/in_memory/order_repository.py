from app.domain.entities.order import Order
from app.domain.repositories.order_repository import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._orders: dict[int, Order] = {}
        self._next_id = 1

    def next_id(self) -> int:
        order_id = self._next_id
        self._next_id += 1

        return order_id

    def save(self, order: Order):
        self._orders[order.id] = order
