from item import Item
from equippable import Equippable
from skill import Skill

def dict_tostr(dictionary: dict) -> str:
    temp = "{ "
    for v in dictionary.values():
        temp += f"{v} "
    temp += "}"
    return temp

class Character:
    inventory: dict[str, Item]
    skills: dict[str, Skill]
    item_in_hand: Item | None

    def __init__(self):
        self.inventory = {}
        self.skills = {}
        self.item_in_hand = None

    def __str__(self) -> str:
        inventory_str = dict_tostr(self.inventory)
        skills_str = dict_tostr(self.skills)
        return f"inv: {inventory_str}\nskills: {skills_str}"

    def give_item(self, item: Item) -> None:
        existing_item = self.inventory.get(item.get_name())
        if existing_item is not None:
            existing_item.set_quantity(existing_item.get_quantity() + 1)
            return
        self.inventory[item.get_name()] = item

    def learn_skill(self, skill: Skill) -> None:
        self.skills[skill.config.name] = skill
    
    def equip(self, equippable: Equippable) -> None:
        equippable.equip()