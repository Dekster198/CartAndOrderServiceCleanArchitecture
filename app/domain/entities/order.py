from datetime import datetime
from enum import Enum


class OrderStatus(Enum):
    UNPAID = 'unpaid'
    PAID = 'paid'
    SHIPPED = 'shipped'
    ACCEPTED = 'accepted'
    CANCELED = 'canceled'


class OrderItem:
    def __init__(self, product_name: str, price: float, quantity: int):
        if not product_name:
            raise ValueError('Product name cannot be empty')
        if price <= 0:
            raise ValueError('Price must be greater than 0')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than 0')

        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        return self.price * self.quantity


class Order:
    def __init__(self, order_id: int, items: list[OrderItem]):
        if not items:
            raise ValueError('Order must contain at least one item')

        self._id = order_id
        self._items = items
        self._status = OrderStatus.UNPAID
        self.created_at = datetime.utcnow()

    @property
    def id(self) -> int:
        return self._id

    @property
    def items(self) -> list[OrderItem]:
        return self._items

    @property
    def status(self):
        return self._status

    @property
    def total_price(self) -> float:
        return sum(item.total_price for item in self._items)

    def pay(self):
        if self._status != OrderStatus.UNPAID:
            raise ValueError('Only unpaid order can be paid')

        self._status = OrderStatus.PAID

    def ship(self):
        if self._status != OrderStatus.PAID:
            raise ValueError('Only paid order can be shipped')
        self._status = OrderStatus.SHIPPED

    def accept(self):
        if self._status != OrderStatus.SHIPPED:
            raise ValueError('Only shipped order can be accepted')
        self._status = OrderStatus.ACCEPTED

    def cancel(self):
        if self._status != OrderStatus.UNPAID:
            raise ValueError('Only unpaid order can be canceled')
        self._status = OrderStatus.CANCELED
