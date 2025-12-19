from abc import ABC, abstractmethod

from app.domain.entities.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def next_id(self) -> int:
        pass

    @abstractmethod
    def save(self, order: Order):
        pass
