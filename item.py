
from equippable import Equippable

class ItemConfig:
    name: str
    max_quantity: int

    def __init__(self, name: str, max_quantity: int) -> None:
        self.name = name
        self.max_quantity = max_quantity

# scrolls
# trinkets
# weapons
# artifacts
# ingredients

class Item:
    config: ItemConfig

    def __init__(self, config: ItemConfig) -> None:
        self.config = config
        self.quantity = 1
        self._equippable = Equippable(self.get_name())

    def __str__(self) -> str:
        return f"{self.get_name()} ({self.quantity})"
    
    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity

    def get_quantity(self) -> int:
        return self.quantity
    
    def get_name(self) -> str:
        return self.config.name
    
    def get_equippable(self) -> Equippable:
        return self._equippable
