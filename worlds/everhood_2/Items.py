from typing import NamedTuple, Optional
from BaseClasses import Item, ItemClassification
from collections import ChainMap
from .Locations import Color

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
    "Floor 23 Key": Everhood2ItemData(106, ItemClassification.progression),
    "Gold Key": Everhood2ItemData(107, ItemClassification.progression),
    "Green Key": Everhood2ItemData(108, ItemClassification.progression), # Todo: Self Lockable.
    "Crimson Bandanna": Everhood2ItemData(109, ItemClassification.useful),
    "Power Gem x2": Everhood2ItemData(110, ItemClassification.progression),
    "Power Gem x3": Everhood2ItemData(111, ItemClassification.progression),
    "Moon Emblem": Everhood2ItemData(112, ItemClassification.progression), # Todo: Is this actually needed?
    "Sun Emblem": Everhood2ItemData(113, ItemClassification.progression), # Todo: Is this actually needed?
    "Stopwatch": Everhood2ItemData(116, ItemClassification.useful),
    "Pinecone Key": Everhood2ItemData(117, ItemClassification.progression),
    "Clover": Everhood2ItemData(118, ItemClassification.useful),
    "Bead Braclet": Everhood2ItemData(119, ItemClassification.useful),
}

# Todo: Do we need level logic?
xp_items: dict[str, Everhood2ItemData] = {
    "0xp": Everhood2ItemData(200, ItemClassification.filler),
    "2xp": Everhood2ItemData(201, ItemClassification.filler),
    "15xp": Everhood2ItemData(202, ItemClassification.filler),
    "20xp": Everhood2ItemData(203, ItemClassification.filler),
    "25xp": Everhood2ItemData(204, ItemClassification.filler),
    "30xp": Everhood2ItemData(205, ItemClassification.filler),
    "35xp": Everhood2ItemData(206, ItemClassification.filler),
    "36xp": Everhood2ItemData(207, ItemClassification.filler),
    "40xp": Everhood2ItemData(208, ItemClassification.filler),
    "45xp": Everhood2ItemData(209, ItemClassification.filler),
    "50xp": Everhood2ItemData(210, ItemClassification.filler),
    "60xp": Everhood2ItemData(211, ItemClassification.filler),
    "64xp": Everhood2ItemData(212, ItemClassification.filler),
    "70xp": Everhood2ItemData(213, ItemClassification.filler),
    "75xp": Everhood2ItemData(214, ItemClassification.filler),
    "76xp": Everhood2ItemData(215, ItemClassification.filler),
    "80xp": Everhood2ItemData(216, ItemClassification.filler),
    "100xp": Everhood2ItemData(217, ItemClassification.filler),
    "128xp": Everhood2ItemData(218, ItemClassification.filler),    
    "150xp": Everhood2ItemData(219, ItemClassification.filler),    
    "192xp": Everhood2ItemData(220, ItemClassification.filler),    
    "200xp": Everhood2ItemData(221, ItemClassification.filler),
    "250xp": Everhood2ItemData(222, ItemClassification.filler),
    "300xp": Everhood2ItemData(223, ItemClassification.filler),
    "350xp": Everhood2ItemData(224, ItemClassification.filler),    
    "400xp": Everhood2ItemData(225, ItemClassification.filler),
    "500xp": Everhood2ItemData(226, ItemClassification.filler),
    "600xp": Everhood2ItemData(227, ItemClassification.filler),
    "650xp": Everhood2ItemData(228, ItemClassification.filler),
    "700xp": Everhood2ItemData(229, ItemClassification.filler),
    "800xp": Everhood2ItemData(230, ItemClassification.filler),
    "888xp": Everhood2ItemData(231, ItemClassification.filler),
    "950xp": Everhood2ItemData(232, ItemClassification.filler),
    "1000xp": Everhood2ItemData(233, ItemClassification.filler),
    "1200xp": Everhood2ItemData(234, ItemClassification.filler),    
    "-2xp": Everhood2ItemData(235, ItemClassification.trap),
    "5xp": Everhood2ItemData(236, ItemClassification.filler),
}

door_randomizer_keys: dict[str, Everhood2ItemData] = {
    "Neon Forest Key": Everhood2ItemData(300, ItemClassification.progression),
    "Progressive Marzian Key": Everhood2ItemData(301, ItemClassification.progression),
    "Eternal War Key": Everhood2ItemData(302, ItemClassification.progression),
    "Smega Console Key": Everhood2ItemData(303, ItemClassification.progression),
    "Lab Key": Everhood2ItemData(304, ItemClassification.progression),
    "Home Town Key": Everhood2ItemData(305, ItemClassification.progression),
}

colors: dict[str, Everhood2ItemData] = {
    "Blue": Everhood2ItemData(350, ItemClassification.progression),
    "Red": Everhood2ItemData(351, ItemClassification.progression),
    "Green": Everhood2ItemData(352, ItemClassification.progression),
    "Yellow": Everhood2ItemData(353, ItemClassification.progression),
    "Brown": Everhood2ItemData(354, ItemClassification.progression),
    "Purple": Everhood2ItemData(355, ItemClassification.progression),
    "Orange": Everhood2ItemData(356, ItemClassification.progression),
}

colors_to_name: dict[Color, str] = {
    Color.blue: "Blue",
    Color.red: "Red",
    Color.green: "Green",
    Color.yellow: "Yellow",
    Color.brown: "Brown",
    Color.purple: "Purple",
    Color.orange: "Orange"
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
    "Hotdog Cosmetic": Everhood2ItemData(408, ItemClassification.filler),
    "Red Bandana Cosmetic": Everhood2ItemData(409, ItemClassification.filler),
    "Oingo Boingo Cosmetic": Everhood2ItemData(410, ItemClassification.filler),
    "Mage Hat Cosmetic": Everhood2ItemData(411, ItemClassification.filler),
    "Afro Cosmetic": Everhood2ItemData(412, ItemClassification.filler),
    "Jester Hat Cosmetic": Everhood2ItemData(413, ItemClassification.filler),
    "Knight Helmet Cosmetic": Everhood2ItemData(414, ItemClassification.filler),
    "Gas Mask Cosmetic": Everhood2ItemData(415, ItemClassification.filler),
}

misc_items: dict[str, Everhood2ItemData] = {
    "Tomato Seed": Everhood2ItemData(114, ItemClassification.filler),
    "Druffle": Everhood2ItemData(115, ItemClassification.filler), # Todo: Filler? Maybe keep the one druffle stuck to Sam
}

all_items: ChainMap[str, Everhood2ItemData] = ChainMap(major_items, xp_items, door_randomizer_keys, cosmetics, misc_items, colors)

item_groups: dict[str, list[str]] = {
    "Soul Weapon": ["Red Soul Axe", "Green Soul Spear", "Blue Soul Knives"],
    "Cosmetic": cosmetics.keys(),
    "XP": xp_items.keys(),
}