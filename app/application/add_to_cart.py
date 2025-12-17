from dataclasses import dataclass


@dataclass
class AddToCartInput:
    product_id: int
    quantity: int


@dataclass
class AddToCartOutput:
    total_price: float


class AddToCartUseCase:
    def __init__(self, product_repo: ProductRepository, cart_repo: CartRepository):
        self.product_repo = product_repo
        self.cart_repo = cart_repo

    def execute(self, data: AddToCartInput) -> AddToCartOutput:
        product = self.product_repo.get_by_id(data.product_id)
        cart = self.cart_repo.get_current()

        product.reserve(data.quantity)
        cart.add_item(
            product_id=product.id,
            product_name=product.name,
            price=product.price,
            quantity=data.quantity
        )

        self.product_repo.save(product)
        self.cart_repo.save(cart)

        return AddToCartOutput(total_price=cart.total_price)
