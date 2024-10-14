
from item import *
from player import *
from character import *
from skill import *

ITEM_CONFIGS = {
    "GOBLET": ItemConfig("goblet", 99),
    "BRONZE_SWORD": ItemConfig("bsword", 1),
    "MYTHRIL_SWORD": ItemConfig("msword", 1),
}

SKILL_CONFIGS = {
    "GOBLET_THROW": SkillConfig("gthrow", ITEM_CONFIGS["GOBLET"])
}

local_player = Player()
local_player.character.give_item(Item(ITEM_CONFIGS["GOBLET"]))
local_player.character.give_item(Item(ITEM_CONFIGS["GOBLET"]))
local_player.character.give_item(Item(ITEM_CONFIGS["BRONZE_SWORD"]))
local_player.character.give_item(Item(ITEM_CONFIGS["MYTHRIL_SWORD"]))

local_player.character.learn_skill(Skill(SKILL_CONFIGS["GOBLET_THROW"]))

local_player.character.equip(local_player.character.inventory["msword"].get_equippable())
local_player.character.equip(local_player.character.skills["gthrow"].get_equippable())

print(str(local_player.character))