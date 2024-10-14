
from typing import Optional
from character import Character

class Ownable:
    _owner: Optional[Character]

    def __init__(self, owner: Optional[Character] = None) -> None:
        self._owner = owner
    
    def get_owner(self) -> Optional[Character]:
        return self._owner
    
    def set_owner(self, owner: Optional[Character]) -> None:
        self._owner = owner

    def is_owned_by(self, character: Character) -> bool:
        return character is self._owner

