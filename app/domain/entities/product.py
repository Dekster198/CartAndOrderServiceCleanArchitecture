class Product:
    def __init__(self, product_id: int, name: str, price: float, stock_quantity: int, description: str | None = None):
        if not name:
            raise ValueError('Name cannot be empty')
        if price <= 0:
            raise ValueError('Price must be greater than 0')
        if stock_quantity < 0:
            raise ValueError('Quantity cannot be negative')

        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
        self._stock_quantity = stock_quantity

    @property
    def stock_quantity(self) -> int:
        return self._stock_quantity

    def reserve(self, quantity: int):
        if quantity <= 0:
            raise ValueError('Quantity must be greater than 0')
        if quantity > self._stock_quantity:
            raise ValueError('Not enough stock to reserve')

        self._stock_quantity -= quantity

    def release(self, quantity: int):
        if quantity <= 0:
            raise ValueError('Quantity must be greater than 0')

        self._stock_quantity += quantity
