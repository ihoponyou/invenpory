
from item import ItemConfig
from equippable import Equippable

# equippable but do not show a model
# weapon skills/spells
# active skills (gaian repair, rigan flood)

class SkillConfig:
    name: str
    required_item: ItemConfig

    def __init__(self, name: str, required_item: ItemConfig) -> None:
        self.name = name
        self.required_item = required_item

class Skill:
    config: SkillConfig

    def __init__(self, config: SkillConfig) -> None:
        self.config = config
        self._equippable = Equippable(self.config.name)
    
    def __str__(self) -> str:
        return self.config.name
    
    def get_equippable(self) -> Equippable:
        return self._equippable