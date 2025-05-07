from typing import Dict, NamedTuple, Optional
from enum import IntEnum
from BaseClasses import Location
from collections import ChainMap


ITEM_LOCATION_START = 100
BATTLE_LOCATION_START = 500

class LocationType(IntEnum):
    item = 0
    hillbert_item = 1
    cosmetic = 2
    hillbert_cosmetic = 3
    major_battle = 4,
    colloseum_battle = 5,
    hillbert_battle = 6,
    trash_battle = 7


class Everhood2Location(Location):
    game: str = "Everhood 2"


class Everhood2LocationData(NamedTuple):
    code: Optional[int]
    region: str
    type: LocationType
    item_name: str


item_locations: Dict[str, Everhood2LocationData] = {    
    "Neon Jungle Chest 1": Everhood2LocationData(ITEM_LOCATION_START, "Neon Jungle", LocationType.item, "50xp"),
    "Neon Jungle Chest 2": Everhood2LocationData(ITEM_LOCATION_START, "Neon Jungle", LocationType.item, "75xp"),
    "Neon Jungle Chest 3": Everhood2LocationData(ITEM_LOCATION_START, "Neon Jungle", LocationType.item, "50xp"),
    "Neon Jungle Chest 4": Everhood2LocationData(ITEM_LOCATION_START, "Neon Jungle", LocationType.item, "75xp"),
    "Neon Jungle Chest 5": Everhood2LocationData(ITEM_LOCATION_START, "Neon Jungle", LocationType.item, "100xp"),
    "Neon Jungle Chest 6": Everhood2LocationData(ITEM_LOCATION_START, "Neon Jungle", LocationType.item, "0xp"),
    "Neon Jungle Power Gem": Everhood2LocationData(ITEM_LOCATION_START, "Neon Jungle", LocationType.item, "Power Gem"),
    
    "Anime Hairstyle": Everhood2LocationData(ITEM_LOCATION_START, "Neon City", LocationType.cosmetic, "Anime Hairstyle"),
    "Mage Hat": Everhood2LocationData(ITEM_LOCATION_START, "Neon City", LocationType.cosmetic, "Mage Hat"),
    "Wild Hairstyle": Everhood2LocationData(ITEM_LOCATION_START, "Neon City", LocationType.cosmetic, "Wild Hairstyle"),
    "Backslick Hairstyle": Everhood2LocationData(ITEM_LOCATION_START, "Neon City", LocationType.cosmetic, "Backslick Hairstyle"),
    "Stylish Hairstyle": Everhood2LocationData(ITEM_LOCATION_START, "Neon City", LocationType.cosmetic, "Stylish Hairstyle"),
    "Natural Hairstyle": Everhood2LocationData(ITEM_LOCATION_START, "Neon City", LocationType.cosmetic, "Natural Hairstyle"), 
    "Afro Hairstyle": Everhood2LocationData(ITEM_LOCATION_START, "Neon City", LocationType.cosmetic, "Afro Hairstyle"),
    
    "Eternal War Battlefield Chest 1": Everhood2LocationData(ITEM_LOCATION_START, "Eternal War - Battlefield", LocationType.item, "100xp"),
    "Hotdog": Everhood2LocationData(ITEM_LOCATION_START, "Eternal War - Battlefield", LocationType.cosmetic, "Hotdog"),
    "Eternal War Battlefield Chest 2": Everhood2LocationData(ITEM_LOCATION_START, "Eternal War - Battlefield", LocationType.item, "50xp"),
    "Eternal War Battlefield Chest 3": Everhood2LocationData(ITEM_LOCATION_START, "Eternal War - Battlefield", LocationType.item, "75xp"),
    "Eternal War Battlefield Chest 4": Everhood2LocationData(ITEM_LOCATION_START, "Eternal War - Battlefield", LocationType.item, "50xp"),
    "Eternal War Battlefield Chest 5": Everhood2LocationData(ITEM_LOCATION_START, "Eternal War - Battlefield", LocationType.item, "50xp"),
    
    "Eternal War Dungeon Chest": Everhood2LocationData(ITEM_LOCATION_START, "Eternal War - Dungeon", LocationType.item, "50xp"),
    "Eternal War Dungeon Power Gem": Everhood2LocationData(ITEM_LOCATION_START, "Eternal War - Dungeon", LocationType.item, "Power Gem"),
    
    "Marzian Era 0 - Mines Chest": Everhood2LocationData(ITEM_LOCATION_START, "Marzian Era 0 - Mining Area", LocationType.item, "50xp"),
    "Marzian Era 0 - Power Gem": Everhood2LocationData(ITEM_LOCATION_START, "Marzian Era 0 - Mining Area", LocationType.item, "Power Gem"),
    
    "Marzian Era 0 - Mining Base Chest": Everhood2LocationData(ITEM_LOCATION_START, "Marzian Era 0 - Mining Base", LocationType.item, "Crimson Bandanna"),
    "Red Bandana": Everhood2LocationData(ITEM_LOCATION_START, "Marzian Era 0 - Mining Base", LocationType.cosmetic, "Red Bandana Cosmetic"),

    "Floor 23 Key": Everhood2LocationData(ITEM_LOCATION_START, "Hillbert Hotel", LocationType.hillbert_item, "Floor 23 Key"),
    "Floor 23 Complete Chest": Everhood2LocationData(ITEM_LOCATION_START, "Hillbert Hotel", LocationType.hillbert_item, "100xp"),
    "Cat Ears": Everhood2LocationData(ITEM_LOCATION_START, "Hillbert Hotel", LocationType.hillbert_cosmetic, "Cat Ears"),
    "Cat Ears Bald": Everhood2LocationData(ITEM_LOCATION_START, "Hillbert Hotel", LocationType.hillbert_cosmetic, "Cat Ears Bald"),
    "Floor Gold Key": Everhood2LocationData(ITEM_LOCATION_START, "Hillbert Hotel", LocationType.hillbert_item, "Floor Gold Key"),
    "Floor Gold Complete Chest": Everhood2LocationData(ITEM_LOCATION_START, "Hillbert Hotel", LocationType.hillbert_item, "50xp"),
    "Oingo Boingo": Everhood2LocationData(ITEM_LOCATION_START, "Hillbert Hotel", LocationType.hillbert_cosmetic, "Oingo Boingo"),
    
    "Floor 23 Smega Reward Chest": Everhood2LocationData(ITEM_LOCATION_START, "Floor 23", LocationType.hillbert_item, "50xp"),
    "Floor 23 Chest 1": Everhood2LocationData(ITEM_LOCATION_START, "Floor 23", LocationType.hillbert_item, "50xp"),
    "Floor 23 Chest 2": Everhood2LocationData(ITEM_LOCATION_START, "Floor 23", LocationType.hillbert_item, "50xp"),
    
    "Floor Gold Chest": Everhood2LocationData(ITEM_LOCATION_START, "Floor Gold", LocationType.hillbert_item, "50xp"),
}

battle_locations: Dict[str, Everhood2LocationData] = {
    # Starting Battle
    "Raven Tutorial Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Tutorial Hub", LocationType.major_battle, "0xp"),
    # Pre Neon City
    "Spring Head Battle 1": Everhood2LocationData(BATTLE_LOCATION_START, "Neon City", LocationType.trash_battle, "20xp"),
    # Neon Jungle Room 1
    "Spring Head Battle 2": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "20xp"),
    "Spring Head Battle 3": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "20xp"),
    "Double Spring Head Battle 1": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "40xp"),
    "Dark Pirahna 1": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "30xp"),
    "Dark Pirahna 2": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "30xp"),
    # Neon Jungle Room 2
    "Homonculus Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.major_battle, "35xp"),
    "Spring Head Battle 4": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "20xp"),
    "Spring Head Battle 5": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "20xp"),
    "Spring Head Battle 6": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "20xp"),
    "Neon String 1": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "50xp"),
    "Dark Pirahna 3": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "30xp"),
    # Neon Jungle Room 3
    "Cowgirl Homonculus Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.major_battle, "36xp"),
    "Double Spring Head Battle 2": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "40xp"),
    "Double Dark Pirahna Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "60xp"),
    "Neon String 2": Everhood2LocationData(BATTLE_LOCATION_START, "Neon Jungle", LocationType.trash_battle, "50xp"),
    
    # Todo: Abyss doesn't have a proper end
    
    # Marzian Era 0 Mines
    "Hyena Battle Screech": Everhood2LocationData(BATTLE_LOCATION_START, "Marzian Era 0 - Mining Area", LocationType.trash_battle, "25xp"),
    "Hyena Battle Warcry": Everhood2LocationData(BATTLE_LOCATION_START, "Marzian Era 0 - Mining Area", LocationType.trash_battle, "25xp"),
    "Shark Battle Bloodnose": Everhood2LocationData(BATTLE_LOCATION_START, "Marzian Era 0 - Mining Area", LocationType.trash_battle, "25xp"),
    "Howler & Razor Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Marzian Era 0 - Mining Area", LocationType.trash_battle, "50xp"),
    "Feugo Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Marzian Era 0 - Mining Area", LocationType.major_battle, "100xp"),

    # Marzian Era 0 Base
    "Insect Abomination Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Marzian Era 0 - Mining Base", LocationType.major_battle, "50xp"),
    "Chase (Bad) Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Marzian Era 0 - Mining Base", LocationType.major_battle, "5xp"),
    "Howler & Razor & Maggot Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Marzian Era 0 - Mining Base", LocationType.trash_battle, "75xp"),
    "Dimension Master Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Marzian Era 0 - Mining Base", LocationType.major_battle, "75xp"),

    # Eternal War Desert
    "Red Onion Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "15xp"),
    "Leek Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "76xp"),
    "Bro-ccoli": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "76xp"),
    "Bell Pepper Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "100xp"),
    "Tomato Rush Lower Left Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Tomato Rush Lower Middle Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Tomato Rush Lower Right Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Tomato Rush Upper Left Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Tomato Rush Upper Middle Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Tomato Rush Upper Right Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Melon Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.major_battle, "100xp"),
    "Chili Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Battlefield", LocationType.trash_battle, "15xp"),

    # Eternal War Castle
    "Capsicum Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Castle", LocationType.major_battle, "15xp"),
    "Carrot Mage Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Castle", LocationType.major_battle, "15xp"),
    "Juice Master#4671 Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Eternal War - Castle", LocationType.major_battle, "15xp"),
    
    # Hillbert Hotel Fights
    # Angry Wizard Todo
    "Hillbert Processor Int Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Floor 23", LocationType.hillbert_battle, "64xp"),
    "Rasputin Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Floor 23", LocationType.hillbert_battle, "100xp"),
    "Bobo (Drunk) Battle": Everhood2LocationData(BATTLE_LOCATION_START, "Floor Gold", LocationType.hillbert_battle, "80xp"),
}

all_locations: ChainMap[str, Everhood2LocationData] = ChainMap(item_locations, battle_locations)