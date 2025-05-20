from typing import NamedTuple, Optional
from BaseClasses import Item, ItemClassification
from collections import ChainMap

class Everhood2Item(Item):
    game: str = "Everhood 2"

class Everhood2ItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler

# Todo: Need to confirm names of various areas.

major_items: dict[str, Everhood2ItemData] = {
    "Power Gem": Everhood2ItemData(100, ItemClassification.progression), # Todo: Give only a couple crystals progression
    "Soul Coin": Everhood2ItemData(101, ItemClassification.progression), # Todo: Give only a couple crystals progression
    "Red Soul Axe": Everhood2ItemData(102, ItemClassification.progression),
    "Green Soul Spear": Everhood2ItemData(103, ItemClassification.progression),
    "Blue Soul Knives": Everhood2ItemData(104, ItemClassification.progression),
    "Katana": Everhood2ItemData(105, ItemClassification.useful),
    "Room 23 Key": Everhood2ItemData(106, ItemClassification.progression),
    "Gold Key": Everhood2ItemData(107, ItemClassification.progression),
    "Green Key": Everhood2ItemData(108, ItemClassification.progression), # Todo: Self Lockable.
    "Crimson Bandanna": Everhood2ItemData(109, ItemClassification.useful),
    "Power Gem x3": Everhood2ItemData(110, ItemClassification.progression),
    "Power Gem x25": Everhood2ItemData(111, ItemClassification.progression),
    "Moon Emblem": Everhood2ItemData(112, ItemClassification.progression), # Todo: Is this actually needed?
    "Sun Emblem": Everhood2ItemData(113, ItemClassification.progression), # Todo: Is this actually needed?
}

# Todo: Do we need level logic?
xp_items: dict[str, Everhood2ItemData] = {
    "0xp": Everhood2ItemData(200, ItemClassification.filler),
    "2xp": Everhood2ItemData(201, ItemClassification.filler),
    # "5xp": Everhood2ItemData(201, ItemClassification.filler),
    "15xp": Everhood2ItemData(202, ItemClassification.filler),
    "20xp": Everhood2ItemData(203, ItemClassification.filler),
    "25xp": Everhood2ItemData(204, ItemClassification.filler),
    "30xp": Everhood2ItemData(205, ItemClassification.filler),
    "35xp": Everhood2ItemData(206, ItemClassification.filler),
    "36xp": Everhood2ItemData(207, ItemClassification.filler),
    "40xp": Everhood2ItemData(208, ItemClassification.filler),
    "50xp": Everhood2ItemData(209, ItemClassification.filler),
    "60xp": Everhood2ItemData(210, ItemClassification.filler),
    "64xp": Everhood2ItemData(211, ItemClassification.filler),
    "70xp": Everhood2ItemData(212, ItemClassification.filler),
    "75xp": Everhood2ItemData(213, ItemClassification.filler),
    "76xp": Everhood2ItemData(214, ItemClassification.filler),
    "80xp": Everhood2ItemData(215, ItemClassification.filler),
    "100xp": Everhood2ItemData(216, ItemClassification.filler),
    "150xp": Everhood2ItemData(217, ItemClassification.filler),
    "200xp": Everhood2ItemData(218, ItemClassification.filler),
    "400xp": Everhood2ItemData(219, ItemClassification.filler),
}

door_randomizer_keys: dict[str, Everhood2ItemData] = {
    "Hillbert Hotel Key": Everhood2ItemData(300, ItemClassification.progression),
    "Eternal War Key": Everhood2ItemData(301, ItemClassification.progression),
    "Marzian Era 0 Key": Everhood2ItemData(302, ItemClassification.progression),
    "Marzian Era 1000 Key": Everhood2ItemData(303, ItemClassification.progression),
    "Marzian Era 2000 Key": Everhood2ItemData(304, ItemClassification.progression),
    "Marzian Era 3000 Key": Everhood2ItemData(305, ItemClassification.progression),
    "Marzian Era 4000 Key": Everhood2ItemData(306, ItemClassification.progression),
    "Marzian Era 5000 Key": Everhood2ItemData(307, ItemClassification.progression),
    "Human Town Key": Everhood2ItemData(308, ItemClassification.progression),
    "Lab Key": Everhood2ItemData(309, ItemClassification.progression),
    "Smega Key": Everhood2ItemData(310, ItemClassification.progression),
    "Mushroom Bureau Key": Everhood2ItemData(311, ItemClassification.progression),
    "4D Dimension Key": Everhood2ItemData(312, ItemClassification.progression),
}

cosmetics: dict[str, Everhood2ItemData] = {
    "Anime Hairstyle Cosmetic": Everhood2ItemData(400, ItemClassification.filler),
    "Wild Hairstyle Cosmetic": Everhood2ItemData(401, ItemClassification.filler),
    "Backslick Hairstyle Cosmetic": Everhood2ItemData(402, ItemClassification.filler),
    "Stylish Hairstyle Cosmetic": Everhood2ItemData(403, ItemClassification.filler),
    "Natural Hairstyle Cosmetic": Everhood2ItemData(404, ItemClassification.filler),
    "Cat Ears Cosmetic": Everhood2ItemData(405, ItemClassification.filler),
    "Cat Ears Bald Cosmetic": Everhood2ItemData(406, ItemClassification.filler),
    "Reindeer Skull Cosmetic": Everhood2ItemData(407, ItemClassification.filler),
    "Hot Dog Cosmetic": Everhood2ItemData(408, ItemClassification.filler),
    "Bandanna Cosmetic": Everhood2ItemData(409, ItemClassification.filler),
    "Oingo Boingo Cosmetic": Everhood2ItemData(410, ItemClassification.filler),
}

misc_items: dict[str, Everhood2ItemData] = {
    "Tomato Seed": Everhood2ItemData(114, ItemClassification.filler),
    "Druffle": Everhood2ItemData(115, ItemClassification.filler), # Todo: Filler? Maybe keep the one druffle stuck to Sam
}

all_items: ChainMap[str, Everhood2ItemData] = ChainMap(major_items, xp_items, cosmetics, misc_items)

item_groups: dict[str, list[str]] = {
    "Soul Weapon": ["Red Soul Axe", "Green Soul Spear", "Blue Soul Knives"],
    "Cosmetic": cosmetics.keys(),
    "XP": xp_items.keys(),
}