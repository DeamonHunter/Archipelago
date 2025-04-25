from typing import NamedTuple, Optional
from BaseClasses import Item, ItemClassification

class Everhood2Item(Item):
    game: str = "Muse Dash"

class Everhood2ItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    count: int = 1 

# Todo: Need to confirm names of various areas.

# Todo: Do we need level logic?
xp_items: dict[str, Everhood2ItemData] = {
    "0xp": Everhood2ItemData(100, ItemClassification.filler),
    "15xp": Everhood2ItemData(100, ItemClassification.filler),
    "20xp": Everhood2ItemData(100, ItemClassification.filler),
    "25xp": Everhood2ItemData(100, ItemClassification.filler),
    "30xp": Everhood2ItemData(100, ItemClassification.filler),
    "35xp": Everhood2ItemData(100, ItemClassification.filler),
    "36xp": Everhood2ItemData(100, ItemClassification.filler),
    "40xp": Everhood2ItemData(100, ItemClassification.filler),
    "50xp": Everhood2ItemData(100, ItemClassification.filler),
    "60xp": Everhood2ItemData(100, ItemClassification.filler),
    "64xp": Everhood2ItemData(100, ItemClassification.filler),
    "75xp": Everhood2ItemData(100, ItemClassification.filler),
    "76xp": Everhood2ItemData(100, ItemClassification.filler),
    "80xp": Everhood2ItemData(100, ItemClassification.filler),
    "100xp": Everhood2ItemData(100, ItemClassification.filler),
    "150xp": Everhood2ItemData(100, ItemClassification.filler),
    "400xp": Everhood2ItemData(100, ItemClassification.filler),
}

major_items: dict[str, Everhood2ItemData] = {
    "Power Gem": Everhood2ItemData(100, ItemClassification.progression), # Todo: Give only a couple crystals progression
    "Soul Coin": Everhood2ItemData(100, ItemClassification.progression), # Todo: Give only a couple crystals progression
    "Red Soul Axe": Everhood2ItemData(100, ItemClassification.progression),
    "Green Soul Spear": Everhood2ItemData(100, ItemClassification.progression),
    "Blue Soul Knives": Everhood2ItemData(100, ItemClassification.progression),
    "Katana": Everhood2ItemData(100, ItemClassification.useful),
    "Room 23 Key": Everhood2ItemData(100, ItemClassification.progression),
    "Gold Key": Everhood2ItemData(100, ItemClassification.progression),
    "Green Key": Everhood2ItemData(100, ItemClassification.progression), # Todo: Self Lockable.
    "Bandanna": Everhood2ItemData(100, ItemClassification.useful),
    "Power Gem x3": Everhood2ItemData(100, ItemClassification.progression),
    "Power Gem x25": Everhood2ItemData(100, ItemClassification.progression),
    "Moon Emblem": Everhood2ItemData(100, ItemClassification.progression), # Todo: Is this actually needed?
    "Sun Emblem": Everhood2ItemData(100, ItemClassification.progression), # Todo: Is this actually needed?
}

door_randomizer_keys: dict[str, Everhood2ItemData] = {
    "Hillbert Hotel Key": Everhood2ItemData(100, ItemClassification.progression),
    "Eternal War Key": Everhood2ItemData(100, ItemClassification.progression),
    "Marzian Era 0 Key": Everhood2ItemData(100, ItemClassification.progression),
    "Marzian Era 1000 Key": Everhood2ItemData(100, ItemClassification.progression),
    "Marzian Era 2000 Key": Everhood2ItemData(100, ItemClassification.progression),
    "Marzian Era 3000 Key": Everhood2ItemData(100, ItemClassification.progression),
    "Marzian Era 4000 Key": Everhood2ItemData(100, ItemClassification.progression),
    "Marzian Era 5000 Key": Everhood2ItemData(100, ItemClassification.progression),
    "Human Town Key": Everhood2ItemData(100, ItemClassification.progression),
    "Lab Key": Everhood2ItemData(100, ItemClassification.progression),
    "Smega Key": Everhood2ItemData(100, ItemClassification.progression),
    "Mushroom Bureau Key": Everhood2ItemData(100, ItemClassification.progression),
    "4D Dimension Key": Everhood2ItemData(100, ItemClassification.progression),
}

cosmetics: dict[str, Everhood2ItemData] = {
    "Anime Hairstyle Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
    "Wild Hairstyle Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
    "Backslick Hairstyle Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
    "Stylish Hairstyle Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
    "Natural Hairstyle Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
    "Cat Ears Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
    "Cat Ears Bald Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
    "Reindeer Skull Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
    "Hot Dog Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
    "Bandanna Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
    "Oingo Boingo Cosmetic": Everhood2ItemData(100, ItemClassification.filler),
}

misc_items: dict[str, Everhood2ItemData] = {
    "Tomato Seed": Everhood2ItemData(100, ItemClassification.filler),
    "Druffle": Everhood2ItemData(100, ItemClassification.filler), # Todo: Filler? Maybe keep the one druffle stuck to Sam
}

groups: dict[str, list[str]] = {
    "Soul Weapon": ["Red Soul Axe", "Green Soul Spear", "Blue Soul Knives"],
    "Cosmetic": cosmetics.values(),
    "XP": xp_items.values(),
}