
from events import Events

class Equippable:
    instance_name: str
    _events: Events
    _is_equipped = False

    def test_on_equip(self):
        print(f"{self.instance_name} equipped")

    def test_on_unequip(self):
        print(f"{self.instance_name} unequipped")
        
    def __init__(self, instance_name: str) -> None:
        self.instance_name = instance_name
        self._events = Events(("on_equip", "on_unequip"))
        self._events.on_equip += self.test_on_equip
        self._events.on_unequip += self.test_on_unequip

    def equip(self):
        self._is_equipped = True
        self._events.on_equip()
    
    def unequip(self):
        self._is_equipped = False
        self._events.on_unequip()