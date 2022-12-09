from typing import Dict

from classes.storage import Gstorage
from error import UnknownProduct


class Shop(Gstorage):
    def __init__(self, items: Dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise UnknownProduct
        super().add(name, amount)
