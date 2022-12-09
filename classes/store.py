from typing import Dict

from classes.storage import Gstorage


class Store(Gstorage):
    def __init__(self, items: Dict[str, int], capacity: int = 100):
        super().__init__(items, capacity)
