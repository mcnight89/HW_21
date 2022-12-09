from typing import Dict

from classes.abstractstorage import Storage
from error import NotEnoughProduct, NotEnoughSpace, UnknownProduct


class Gstorage(Storage):
    def __init__(self, items: Dict[str, int], capacity: int):
        super().__init__(items, capacity)
        self.items = items
        self.capacity = capacity

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() < amount:
            raise NotEnoughSpace
        self._items[name] = self._items.get(name, 0) + amount

    def remove(self, name: str, amount: int) -> None:
        if name not in self._items:
            raise UnknownProduct
        if self._items[name] < amount:
            raise NotEnoughProduct
        self._items[name] -= amount
        if self._items[name] == 0:
            self._items.pop(name)

    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self) -> Dict[str, int]:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items)
