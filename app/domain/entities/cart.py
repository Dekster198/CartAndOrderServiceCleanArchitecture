class CartItem:
    def __init__(self, product_id: int, product_name: str, price: float, quantity: int):
        if not product_name:
            raise ValueError('Product name cannot be empty')
        if price <= 0:
            raise ValueError('Price must be greater than 0')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than 0')

        self.product_id = product_id
        self.product_name = product_name
        self._price = price
        self._quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @property
    def quantity(self) -> int:
        return self._quantity

    def increase(self, quantity: int):
        if quantity <= 0:
            raise ValueError('Quantity must be greater than 0')

        self._quantity += quantity


class Cart:
    def __init__(self):
        self._items: dict[int, CartItem] = {}

    def add_item(self, product_id: int, product_name: str, price: float, quantity: int):
        if product_id in self._items:
            self._items[product_id].increase(quantity)
        else:
            self._items[product_id] = CartItem(product_id, product_name, price, quantity)

    def remove_item(self, product_id: int):
        if product_id not in self._items:
            raise ValueError('Item not found in cart')

        del self._items[product_id]

    def clear(self):
        self._items.clear()

    def is_empty(self) -> bool:
        return not self._items

    def items(self) -> list[CartItem]:
        return list(self._items.values())

    @property
    def total_price(self) -> float:
        return sum(item.price * item.quantity for item in self._items.values())
