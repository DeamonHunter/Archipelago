from typing import Dict, NamedTuple, Optional
from enum import IntFlag
from BaseClasses import Location
from collections import ChainMap


ITEM_LOCATION_START = 100
BATTLE_LOCATION_START = 500


class LocationType(IntFlag):
    item = 1 << 0
    cosmetic = 1 << 1
    major_battle = 1 << 2
    unique_battle = 1 << 3
    trash_battle = 1 << 4
    
    hillbert = 1 << 5
    colosseum = 1 << 6
    pre_dragon_doors = 1 << 7
    post_dragon = 1 << 8
    post_game = 1 << 8


class Everhood2Location(Location):
    game: str = "Everhood 2"


class Everhood2LocationData(NamedTuple):
    code: Optional[int]
    region: str
    type: LocationType
    item_name: str


class Everhood2EventData(NamedTuple):
    region: str
    type: LocationType


item_locations: Dict[str, Everhood2LocationData] = {    
    "Neon Jungle Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 0, "Neon Jungle", LocationType.item, "50xp"),
    "Neon Jungle Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 1, "Neon Jungle", LocationType.item, "75xp"),
    "Neon Jungle Chest 3": Everhood2LocationData(ITEM_LOCATION_START + 2, "Neon Jungle", LocationType.item, "50xp"),
    "Neon Jungle Chest 4": Everhood2LocationData(ITEM_LOCATION_START + 3, "Neon Jungle", LocationType.item, "75xp"),
    "Neon Jungle Chest 5": Everhood2LocationData(ITEM_LOCATION_START + 4, "Neon Jungle", LocationType.item, "100xp"),
    "Neon Jungle Chest 6": Everhood2LocationData(ITEM_LOCATION_START + 5, "Neon Jungle", LocationType.item, "0xp"),
    "Neon Jungle Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 6, "Neon Jungle", LocationType.item, "Power Gem"),
    
    "Anime Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 7, "Neon City", LocationType.cosmetic, "Anime Hairstyle Cosmetic"),
    "Mage Hat Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 8, "Neon City", LocationType.cosmetic, "Mage Hat Cosmetic"),
    "Wild Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 9, "Neon City", LocationType.cosmetic, "Wild Hairstyle Cosmetic"),
    "Backslick Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 10, "Neon City", LocationType.cosmetic, "Backslick Hairstyle Cosmetic"),
    "Stylish Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 11, "Neon City", LocationType.cosmetic, "Stylish Hairstyle Cosmetic"),
    "Natural Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 12, "Neon City", LocationType.cosmetic, "Natural Hairstyle Cosmetic"), 
    "Afro Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 13, "Neon City", LocationType.cosmetic, "Afro Cosmetic"),
    
    "Eternal War Battlefield Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 14, "Eternal War - Battlefield", LocationType.item, "100xp"),
    "Hotdog Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 15, "Eternal War - Battlefield", LocationType.cosmetic, "Hotdog Cosmetic"),
    "Eternal War Battlefield Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 16, "Eternal War - Battlefield", LocationType.item, "50xp"),
    "Eternal War Battlefield Chest 3": Everhood2LocationData(ITEM_LOCATION_START + 17, "Eternal War - Battlefield", LocationType.item, "75xp"),
    "Eternal War Battlefield Chest 4": Everhood2LocationData(ITEM_LOCATION_START + 18, "Eternal War - Battlefield", LocationType.item, "50xp"),
    "Eternal War Battlefield Chest 5": Everhood2LocationData(ITEM_LOCATION_START + 19, "Eternal War - Battlefield", LocationType.item, "50xp"),
    
    "Eternal War Dungeon Chest": Everhood2LocationData(ITEM_LOCATION_START + 20, "Eternal War - Dungeon", LocationType.item, "50xp"),
    "Eternal War Dungeon Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 21, "Eternal War - Dungeon", LocationType.item, "Power Gem"),
    
    "Marzian Era 0 - Mines Chest": Everhood2LocationData(ITEM_LOCATION_START + 22, "Marzian Era 0 - Mining Area", LocationType.item, "50xp"),
    "Marzian Era 0 - Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 23, "Marzian Era 0 - Mining Area", LocationType.item, "Power Gem"),
    
    "Marzian Era 0 - Mining Base Chest": Everhood2LocationData(ITEM_LOCATION_START + 24, "Marzian Era 0 - Mining Base", LocationType.item, "Crimson Bandanna"),
    "Red Bandana Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 25, "Marzian Era 0 - Mining Base", LocationType.cosmetic, "Red Bandana Cosmetic"),

    "Floor 23 Key": Everhood2LocationData(ITEM_LOCATION_START + 26, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "Floor 23 Key"),
    "Floor 23 Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 27, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "100xp"),
    "Cat Ears": Everhood2LocationData(ITEM_LOCATION_START + 28, "Hillbert Hotel", LocationType.cosmetic | LocationType.hillbert, "Cat Ears Cosmetic"),
    "Cat Ears Bald": Everhood2LocationData(ITEM_LOCATION_START + 29, "Hillbert Hotel", LocationType.cosmetic | LocationType.hillbert, "Cat Ears Bald Cosmetic"),
    "Gold Key": Everhood2LocationData(ITEM_LOCATION_START + 30, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "Gold Key"),
    "Floor Gold Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 31, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "50xp"),
    "Oingo Boingo": Everhood2LocationData(ITEM_LOCATION_START + 32, "Hillbert Hotel", LocationType.cosmetic | LocationType.hillbert, "Oingo Boingo Cosmetic"),

    "Floor 23 Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 33, "Floor 23", LocationType.item | LocationType.hillbert, "50xp"),
    "Floor 23 Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 34, "Floor 23", LocationType.item | LocationType.hillbert, "50xp"),
    "Floor 23 Smega Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 35, "Floor 23", LocationType.item | LocationType.hillbert, "50xp"),
    
    "Floor Gold Chest": Everhood2LocationData(ITEM_LOCATION_START + 36, "Floor Gold", LocationType.item | LocationType.hillbert, "50xp"),
    "Green Key": Everhood2LocationData(ITEM_LOCATION_START + 37, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "Green Key"),
    
    "Stopwatch Artifact": Everhood2LocationData(ITEM_LOCATION_START + 39, "Infinity Hub", LocationType.item, "Stopwatch"), # Technically in tutorial area, but not modelling that.
    
    "Floor Green Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 41, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "Power Gem"),
    "Pinecone Key": Everhood2LocationData(ITEM_LOCATION_START + 42, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "Pinecone Key"),
    "Floor Pinecone Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 43, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "Power Gem"),
    "Reindeer Skull": Everhood2LocationData(ITEM_LOCATION_START + 44, "Hillbert Hotel", LocationType.cosmetic | LocationType.hillbert, "Reindeer Skull Cosmetic"),
    # "Floor Omega Key": Everhood2LocationData(ITEM_LOCATION_START + 45, "Hillbert Hotel", LocationType.item | LocationType.hillbert | LocationType.post_dragon, "Omega Key"),
    # "Floor Omega Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 46, "Hillbert Hotel", LocationType.item | LocationType.hillbert | LocationType.post_dragon, "Power Gem"),
    # "Jester Hat": Everhood2LocationData(ITEM_LOCATION_START + 47, "Hillbert Hotel", LocationType.cosmetic | LocationType.hillbert | LocationType.post_dragon, "Jester Hat Cosmetic"),
    
    "Floor Pinecone Chest": Everhood2LocationData(ITEM_LOCATION_START + 48, "Floor Pinecone", LocationType.item | LocationType.hillbert, "50xp"),
    
    # "Marzian Era 3000 Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 49, "Marzian Era 3000", LocationType.item | LocationType.post_dragon, "100xp"),
    # "Marzian Era 3000 Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 50, "Marzian Era 3000", LocationType.item | LocationType.post_dragon, "50xp"),

    # "Marzian Era 4000 Chest": Everhood2LocationData(ITEM_LOCATION_START + 51, "Marzian Era 4000", LocationType.item | LocationType.post_dragon, "Power Gem"),

    # "Sun Insignia": Everhood2LocationData(ITEM_LOCATION_START + 52, "Mushroom Bureau - Sun", LocationType.item | LocationType.post_dragon, "Sun Insignia"),
    # "Mushroom Bureau Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 53, "Mushroom Bureau - Moon", LocationType.item | LocationType.post_dragon, "Power Gem"),
    # "Moon Insignia": Everhood2LocationData(ITEM_LOCATION_START + 54, "Mushroom Bureau - Moon", LocationType.item | LocationType.post_dragon, "Moon Insignia"),
    # "Mushroom Bureau Death Coin": Everhood2LocationData(ITEM_LOCATION_START + 55, "Mushroom Bureau - Moon", LocationType.item | LocationType.post_dragon, "Death Coin"),

    # "Duality Artifact": Everhood2LocationData(ITEM_LOCATION_START + 56, "Lucy's Room", LocationType.item | LocationType.post_dragon, "Duality"),
    
    # Todo: Do we replace this with a progressive green key?
    # "Crystal Key": Everhood2LocationData(ITEM_LOCATION_START + 57, "Sam's Room", LocationType.item | LocationType.post_dragon, "Crystal Key"),

    # Todo: Determine how soul weapons are placed.
    # "Marzian Soul Weapon": Everhood2LocationData(ITEM_LOCATION_START + 58, "Marzian Era 4000", LocationType.item | LocationType.post_dragon, "Green Soul Spear"),

    # Todo: Correct Names
    "Lab Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 59, "Lab", LocationType.item | LocationType.pre_dragon_doors, "35xp"),
    "Clover Artifact": Everhood2LocationData(ITEM_LOCATION_START + 60, "Lab", LocationType.item | LocationType.pre_dragon_doors, "Clover"),
    "Lab Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 61, "Lab", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),

    # "Floor Omega Chest": Everhood2LocationData(ITEM_LOCATION_START + 62, "Floor Omega", LocationType.item | LocationType.post_dragon, "Power Gem"),

    # "Liminal Room Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 63, "Liminal Room", LocationType.item | LocationType.post_dragon, "Power Gem"), 
    # "Liminal Room Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 64, "Liminal Room", LocationType.item | LocationType.post_dragon, "Power Gem"),

    # Todo: Give more Descriptive names
    "Smega Console Start Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 65, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console Start Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 66, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console Start Chest 3": Everhood2LocationData(ITEM_LOCATION_START + 67, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console Audio Chest": Everhood2LocationData(ITEM_LOCATION_START + 68, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Gas Mask Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 69, "Smega Console", LocationType.cosmetic | LocationType.pre_dragon_doors, "Gas Mask Cosmetic"),
    "Doctor Dump Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 70, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console RAM Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 71, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console RAM Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 72, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "100xp"),
    "Smega Console RAM Chest 3": Everhood2LocationData(ITEM_LOCATION_START + 73, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console RAM Chest 4": Everhood2LocationData(ITEM_LOCATION_START + 74, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console RAM Chest 5": Everhood2LocationData(ITEM_LOCATION_START + 75, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console RAM Chest 6": Everhood2LocationData(ITEM_LOCATION_START + 76, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console RAM Chest 7": Everhood2LocationData(ITEM_LOCATION_START + 77, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console RAM Chest 8": Everhood2LocationData(ITEM_LOCATION_START + 78, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console RAM Chest 9": Everhood2LocationData(ITEM_LOCATION_START + 79, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console RAM Chest 10": Everhood2LocationData(ITEM_LOCATION_START + 80, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console RAM Chest 11": Everhood2LocationData(ITEM_LOCATION_START + 81, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console RAM Chest 12": Everhood2LocationData(ITEM_LOCATION_START + 82, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console Processor Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 83, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console Processor Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 84, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console Processor Chest 3": Everhood2LocationData(ITEM_LOCATION_START + 85, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console Processor Chest 4": Everhood2LocationData(ITEM_LOCATION_START + 86, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console Processor Chest 5": Everhood2LocationData(ITEM_LOCATION_START + 87, "Smega Console", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    
    # Todo: More Descriptive Names
    # "Death Mountain Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 88, "Death Mountain", LocationType.item | LocationType.post_dragon, "50xp"),
    # "Death Mountain Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 89, "Death Mountain", LocationType.item | LocationType.post_dragon, "Power Gem"),
    # "Death Mountain Chest 3": Everhood2LocationData(ITEM_LOCATION_START + 90, "Death Mountain", LocationType.item | LocationType.post_dragon, "Power Gem"),
    # "Death Mountain Chest 4": Everhood2LocationData(ITEM_LOCATION_START + 91, "Death Mountain", LocationType.item | LocationType.post_dragon, "50xp"),
    # "Death Mountain Chest 5": Everhood2LocationData(ITEM_LOCATION_START + 92, "Death Mountain", LocationType.item | LocationType.post_dragon, "50xp"),
    # "Death Mountain Chest 6": Everhood2LocationData(ITEM_LOCATION_START + 93, "Death Mountain", LocationType.item | LocationType.post_dragon, "50xp"),
    # "Death Mountain Death Coin": Everhood2LocationData(ITEM_LOCATION_START + 94, "Death Mountain", LocationType.item | LocationType.post_dragon, "Death Coin"),
    # "Death Mountain Chest 8": Everhood2LocationData(ITEM_LOCATION_START + 95, "Death Mountain", LocationType.item | LocationType.post_dragon, "50xp"),

    # "V.I.P. Ticket": Everhood2LocationData(ITEM_LOCATION_START + 96, "Everhood 1", LocationType.item | LocationType.post_dragon, "V.I.P. Ticket"),
    # "Long Plank": Everhood2LocationData(ITEM_LOCATION_START + 97, "Everhood 1", LocationType.item | LocationType.post_dragon, "Long Plank"),
    # "Yellow Mask": Everhood2LocationData(ITEM_LOCATION_START + 98, "Everhood 1", LocationType.item | LocationType.post_dragon, "Yellow Mask"),
    # "Everhood 1 Death Coin": Everhood2LocationData(ITEM_LOCATION_START + 99, "Everhood 1", LocationType.item | LocationType.post_dragon, "Death Coin"),
    # "Light Being Soul Weapon": Everhood2LocationData(ITEM_LOCATION_START + 100, "Everhood 1", LocationType.item | LocationType.post_dragon, "Blue Soul Knives"),

    # "Colosseum Reward 1": Everhood2LocationData(ITEM_LOCATION_START + 101, "Colosseum", LocationType.item | LocationType.colosseum, "Power Gem"),
    # "Knight Helmet Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 102, "Colosseum", LocationType.cosmetic | LocationType.colosseum, "Knight Helmet Cosmetic"),
    # "Colosseum Reward 2": Everhood2LocationData(ITEM_LOCATION_START + 103, "Colosseum", LocationType.item | LocationType.colosseum, "Death Coin"),
    # "Colosseum Reward 3": Everhood2LocationData(ITEM_LOCATION_START + 104, "Colosseum", LocationType.item | LocationType.colosseum, "Power Gem x2"),
    # "Colosseum Reward 4": Everhood2LocationData(ITEM_LOCATION_START + 105, "Colosseum", LocationType.item | LocationType.colosseum, "Power Gem x3"),
    # "Colosseum Reward 5": Everhood2LocationData(ITEM_LOCATION_START + 106, "Colosseum", LocationType.item | LocationType.colosseum | LocationType.post_game, "Power Gem x2"),
    # "Colosseum Reward 6": Everhood2LocationData(ITEM_LOCATION_START + 107, "Colosseum", LocationType.item | LocationType.colosseum | LocationType.post_game, "Power Gem x2"),

    # "Pandemonium Chest": Everhood2LocationData(ITEM_LOCATION_START + 108, "Colosseum", LocationType.item | LocationType.post_dragon, "Power Gem"),
    # "Torment Room Chest": Everhood2LocationData(ITEM_LOCATION_START + 109, "Colosseum", LocationType.item | LocationType.post_dragon, "Power Gem"),
    
    "Katana": Everhood2LocationData(ITEM_LOCATION_START + 110, "Lab", LocationType.item | LocationType.pre_dragon_doors, "Katana"), 
    # "Dragon Soul Weapon": Everhood2LocationData(ITEM_LOCATION_START + 111, "Raven Hub", LocationType.item | LocationType.post_dragon, "Red Soul Axe"),
    "Pet the Orange Cat": Everhood2LocationData(ITEM_LOCATION_START + 112, "Home Town", LocationType.item | LocationType.pre_dragon_doors, "5xp"),
    "Pet the Grey Cat": Everhood2LocationData(ITEM_LOCATION_START + 113, "Home Town", LocationType.item | LocationType.pre_dragon_doors, "5xp"),
    "Pet the Black Cat": Everhood2LocationData(ITEM_LOCATION_START + 114, "Home Town", LocationType.item | LocationType.pre_dragon_doors, "-2xp"),
    "Bead Braclet": Everhood2LocationData(ITEM_LOCATION_START + 115, "Home Town", LocationType.item | LocationType.pre_dragon_doors, "Bead Braclet"),
}

battle_locations: Dict[str, Everhood2LocationData] = {
    # Starting Battle
    "Raven Tutorial Battle": Everhood2LocationData(BATTLE_LOCATION_START + 0, "Tutorial Hub", LocationType.major_battle, "0xp"),
    # Pre Neon City
    "Spring Head Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 1, "Neon City", LocationType.trash_battle, "20xp"),
    # Neon Jungle Room 1
    "Spring Head Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 2, "Neon Jungle", LocationType.trash_battle, "20xp"),
    "Spring Head Battle 3": Everhood2LocationData(BATTLE_LOCATION_START + 3, "Neon Jungle", LocationType.trash_battle, "20xp"),
    "Double Spring Head Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 4, "Neon Jungle", LocationType.trash_battle, "40xp"),
    "Dark Pirahna 1": Everhood2LocationData(BATTLE_LOCATION_START + 5, "Neon Jungle", LocationType.trash_battle, "30xp"),
    "Dark Pirahna 2": Everhood2LocationData(BATTLE_LOCATION_START + 6, "Neon Jungle", LocationType.trash_battle, "30xp"),
    # Neon Jungle Room 2
    "Homonculus Battle": Everhood2LocationData(BATTLE_LOCATION_START + 7, "Neon Jungle", LocationType.major_battle, "35xp"),
    "Spring Head Battle 4": Everhood2LocationData(BATTLE_LOCATION_START + 8, "Neon Jungle", LocationType.trash_battle, "20xp"),
    "Spring Head Battle 5": Everhood2LocationData(BATTLE_LOCATION_START + 9, "Neon Jungle", LocationType.trash_battle, "20xp"),
    "Spring Head Battle 6": Everhood2LocationData(BATTLE_LOCATION_START + 10, "Neon Jungle", LocationType.trash_battle, "20xp"),
    "Neon String 1": Everhood2LocationData(BATTLE_LOCATION_START + 11, "Neon Jungle", LocationType.trash_battle, "50xp"),
    "Dark Pirahna 3": Everhood2LocationData(BATTLE_LOCATION_START + 12, "Neon Jungle", LocationType.trash_battle, "30xp"),
    # Neon Jungle Room 3
    "Cowgirl Homonculus Battle": Everhood2LocationData(BATTLE_LOCATION_START + 13, "Neon Jungle", LocationType.major_battle, "36xp"),
    "Double Spring Head Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 14, "Neon Jungle", LocationType.trash_battle, "40xp"),
    "Double Dark Pirahna Battle": Everhood2LocationData(BATTLE_LOCATION_START + 15, "Neon Jungle", LocationType.trash_battle, "60xp"),
    "Neon String 2": Everhood2LocationData(BATTLE_LOCATION_START + 16, "Neon Jungle", LocationType.trash_battle, "50xp"),
    
    # Todo: Abyss doesn't have a proper end
    
    # Marzian Era 0 Mines
    "Hyena Battle Screech": Everhood2LocationData(BATTLE_LOCATION_START + 18, "Marzian Era 0 - Mining Area", LocationType.trash_battle, "25xp"),
    "Hyena Battle Warcry": Everhood2LocationData(BATTLE_LOCATION_START + 19, "Marzian Era 0 - Mining Area", LocationType.trash_battle, "25xp"),
    "Shark Battle Bloodnose": Everhood2LocationData(BATTLE_LOCATION_START + 20, "Marzian Era 0 - Mining Area", LocationType.trash_battle, "25xp"),
    "Howler & Razor Battle": Everhood2LocationData(BATTLE_LOCATION_START + 21, "Marzian Era 0 - Mining Area", LocationType.major_battle, "50xp"),
    "Feugo Battle": Everhood2LocationData(BATTLE_LOCATION_START + 22, "Marzian Era 0 - Mining Area", LocationType.major_battle, "100xp"),

    # Marzian Era 0 Base
    "Insect Abomination Battle": Everhood2LocationData(BATTLE_LOCATION_START + 23, "Marzian Era 0 - Mining Base", LocationType.major_battle, "50xp"),
    "Anxious Chase Battle": Everhood2LocationData(BATTLE_LOCATION_START + 24, "Marzian Era 0 - Mining Base", LocationType.major_battle, "2xp"),
    "Howler & Razor & Maggot Battle": Everhood2LocationData(BATTLE_LOCATION_START + 25, "Marzian Era 0 - Mining Base", LocationType.trash_battle, "75xp"),
    "Dimension Master Battle": Everhood2LocationData(BATTLE_LOCATION_START + 26, "Marzian Era 0 - Mining Base", LocationType.major_battle, "200xp"),
    
    "Dimension Portal Battle": Everhood2LocationData(BATTLE_LOCATION_START + 27, "Marzian Era 1000", LocationType.major_battle, "400xp"),
    "Blue Stonegrunt Battle": Everhood2LocationData(BATTLE_LOCATION_START + 28, "Marzian Era 2000", LocationType.major_battle, "150xp"),

    # Eternal War Desert
    "Red Onion Battle": Everhood2LocationData(BATTLE_LOCATION_START + 29, "Eternal War - Battlefield", LocationType.trash_battle, "15xp"),
    "Leek Battle": Everhood2LocationData(BATTLE_LOCATION_START + 30, "Eternal War - Battlefield", LocationType.unique_battle, "76xp"),
    "Bro-ccoli": Everhood2LocationData(BATTLE_LOCATION_START + 31, "Eternal War - Battlefield", LocationType.unique_battle, "76xp"),
    "Bell Pepper Battle": Everhood2LocationData(BATTLE_LOCATION_START + 32, "Eternal War - Battlefield", LocationType.unique_battle, "100xp"),
    "Tomato Rush Lower Left Battle": Everhood2LocationData(BATTLE_LOCATION_START + 33, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Tomato Rush Lower Middle Battle": Everhood2LocationData(BATTLE_LOCATION_START + 34, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Tomato Rush Lower Right Battle": Everhood2LocationData(BATTLE_LOCATION_START + 35, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Tomato Rush Upper Left Battle": Everhood2LocationData(BATTLE_LOCATION_START + 36, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Tomato Rush Upper Middle Battle": Everhood2LocationData(BATTLE_LOCATION_START + 37, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Tomato Rush Upper Right Battle": Everhood2LocationData(BATTLE_LOCATION_START + 38, "Eternal War - Battlefield", LocationType.trash_battle, "25xp"),
    "Melon Battle": Everhood2LocationData(BATTLE_LOCATION_START + 39, "Eternal War - Battlefield", LocationType.major_battle, "100xp"),
    "Chili Battle": Everhood2LocationData(BATTLE_LOCATION_START + 40, "Eternal War - Battlefield", LocationType.unique_battle, "15xp"),

    # Eternal War Castle
    "Capsicum Battle": Everhood2LocationData(BATTLE_LOCATION_START + 41, "Eternal War - Castle", LocationType.major_battle, "70xp"),
    "Carrot Mage Battle": Everhood2LocationData(BATTLE_LOCATION_START + 42, "Eternal War - Castle", LocationType.major_battle, "45xp"),
    "Juice Master#4671 Battle": Everhood2LocationData(BATTLE_LOCATION_START + 43, "Eternal War - Castle", LocationType.major_battle, "150xp"),
    
    # Hillbert Hotel Fights
    # Angry Wizard Todo
    "Hillbert Processor Int Battle": Everhood2LocationData(BATTLE_LOCATION_START + 45, "Floor 23", LocationType.unique_battle | LocationType.hillbert, "64xp"),
    "Rasputin Battle": Everhood2LocationData(BATTLE_LOCATION_START + 46, "Floor 23", LocationType.major_battle | LocationType.hillbert, "100xp"),
    "Bobo (Drunk) Battle": Everhood2LocationData(BATTLE_LOCATION_START + 47, "Floor Gold", LocationType.major_battle | LocationType.hillbert, "80xp"),
    
    "Squirrels Battle": Everhood2LocationData(BATTLE_LOCATION_START + 48, "Floor Pinecone", LocationType.major_battle | LocationType.hillbert, "400xp"),
    
    "Opus & Screech Battle": Everhood2LocationData(BATTLE_LOCATION_START + 50, "Marzian Era 0 - Mining Base", LocationType.trash_battle, "80xp"),

    # "Thriller Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 51, "Marzian Era 3000", LocationType.trash_battle | LocationType.post_dragon, "50xp"),
    # "Lurker Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 52, "Marzian Era 3000", LocationType.trash_battle | LocationType.post_dragon, "50xp"),
    # "Lurker Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 53, "Marzian Era 3000", LocationType.trash_battle | LocationType.post_dragon, "50xp"),
    # "Wheeler Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 54, "Marzian Era 3000", LocationType.trash_battle | LocationType.post_dragon, "50xp"),
    # "Lurker Battle 3": Everhood2LocationData(BATTLE_LOCATION_START + 55, "Marzian Era 3000", LocationType.trash_battle | LocationType.post_dragon, "50xp"),
    # "Wheeler Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 56, "Marzian Era 3000", LocationType.trash_battle | LocationType.post_dragon, "50xp"),
    # "Thriller Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 57, "Marzian Era 3000", LocationType.trash_battle | LocationType.post_dragon, "50xp"),

    # "Lurker Battle (Era 4000)": Everhood2LocationData(BATTLE_LOCATION_START + 58, "Marzian Era 4000", LocationType.trash_battle | LocationType.post_dragon, "50xp"),
    # "Marzian Battle": Everhood2LocationData(BATTLE_LOCATION_START + 59, "Marzian Era 4000", LocationType.major_battle | LocationType.post_dragon, "50xp"),
    # "True Chase Battle": Everhood2LocationData(BATTLE_LOCATION_START + 60, "Marzian Era 4000", LocationType.major_battle | LocationType.post_dragon, "75xp"),
    # "Shark Jailor (Era 4000)": Everhood2LocationData(BATTLE_LOCATION_START + 61, "Marzian Era 4000", LocationType.trash_battle | LocationType.post_dragon, "25xp"),
    # "Feugo Battle (Era 4000)": Everhood2LocationData(BATTLE_LOCATION_START + 62, "Marzian Era 4000", LocationType.major_battle | LocationType.post_dragon, "100xp"),

    # "Brown Slow Mushroom Sun Battle": Everhood2LocationData(BATTLE_LOCATION_START + 63, "Mushroom Bureau - Sun", LocationType.major_battle | LocationType.post_dragon, "50xp"), # Todo: Are both mushroom fights the same?
    # "Hydra Mushroom Battle": Everhood2LocationData(BATTLE_LOCATION_START + 64, "Mushroom Bureau - Moon", LocationType.unique_battle | LocationType.post_dragon, "50xp"),
    # "Smelly Gas Mushroom Battle": Everhood2LocationData(BATTLE_LOCATION_START + 65, "Mushroom Bureau - Moon", LocationType.unique_battle | LocationType.post_dragon, "50xp"),
    # "Brown Slow Mushroom Moon Battle": Everhood2LocationData(BATTLE_LOCATION_START + 66, "Mushroom Bureau - Moon", LocationType.unique_battle | LocationType.post_dragon, "50xp"),
    # "Sun Knight Battle": Everhood2LocationData(BATTLE_LOCATION_START + 67, "Mushroom Bureau - Sun", LocationType.major_battle | LocationType.post_dragon, "100xp"),
    # "Judge Mushroom Battle": Everhood2LocationData(BATTLE_LOCATION_START + 68, "Mushroom Bureau - Finale", LocationType.major_battle | LocationType.post_dragon, "100xp"),
    
    # "Lucy Battle": Everhood2LocationData(BATTLE_LOCATION_START + 69, "Lucy's Room", LocationType.unique_battle | LocationType.post_dragon, "1000xp"),

    # "Jest 3D Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 70, "Irvine Pocket Dimension", LocationType.trash_battle | LocationType.post_dragon, "100xp"),
    # "Jest 3D Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 71, "Irvine Pocket Dimension", LocationType.trash_battle | LocationType.post_dragon, "100xp"),
    # "Doopy Dragon 3D Battle": Everhood2LocationData(BATTLE_LOCATION_START + 72, "Irvine Pocket Dimension", LocationType.unique_battle | LocationType.post_dragon, "35xp"),
    # "Vanguard 3D Battle": Everhood2LocationData(BATTLE_LOCATION_START + 73, "Irvine Pocket Dimension", LocationType.major_battle | LocationType.post_dragon, "250xp"),
    
    "Door of the Dead Battle": Everhood2LocationData(BATTLE_LOCATION_START + 74, "Lab", LocationType.unique_battle | LocationType.pre_dragon_doors, "0xp"),
    "Ghost Chunky Battle": Everhood2LocationData(BATTLE_LOCATION_START + 75, "Lab", LocationType.unique_battle | LocationType.pre_dragon_doors, "35xp"),
    "Ghost Junkie Battle": Everhood2LocationData(BATTLE_LOCATION_START + 76, "Lab", LocationType.unique_battle | LocationType.pre_dragon_doors, "35xp"),
    "Ghost Franky Battle": Everhood2LocationData(BATTLE_LOCATION_START + 77, "Lab", LocationType.major_battle | LocationType.pre_dragon_doors, "35xp"),

    # "Cazok Carrot Battle": Everhood2LocationData(BATTLE_LOCATION_START + 78, "Floor Omega", LocationType.unique_battle | LocationType.post_dragon, "50xp"),
    # "Cazok Ghost Battle": Everhood2LocationData(BATTLE_LOCATION_START + 79, "Floor Omega", LocationType.unique_battle | LocationType.post_dragon, "50xp"),
    # "Cazok Vanguard 3D Battle": Everhood2LocationData(BATTLE_LOCATION_START + 80, "Floor Omega", LocationType.unique_battle | LocationType.post_dragon, "50xp"),
    # "Cazok Battle": Everhood2LocationData(BATTLE_LOCATION_START + 81, "Floor Omega", LocationType.major_battle | LocationType.post_dragon, "950xp"),

    #Todo Categorise Better
    "Motherboard INT Battle": Everhood2LocationData(BATTLE_LOCATION_START + 82, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "Motherboard CHAR Battle": Everhood2LocationData(BATTLE_LOCATION_START + 83, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "Motherboard BOOL x3 Battle": Everhood2LocationData(BATTLE_LOCATION_START + 84, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "192xp"),
    "Motherboard While Battle": Everhood2LocationData(BATTLE_LOCATION_START + 85, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    
    "RAM INT Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 86, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "RAM BOOL Battle": Everhood2LocationData(BATTLE_LOCATION_START + 87, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "RAM While Battle": Everhood2LocationData(BATTLE_LOCATION_START + 88, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "RAM While x2 Battle": Everhood2LocationData(BATTLE_LOCATION_START + 89, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "128xp"),
    "RAM INT Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 90, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "RAM CHAR Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 91, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "RAM FLOAT Battle": Everhood2LocationData(BATTLE_LOCATION_START + 92, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "RAM CHAR Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 93, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "RAM MATRIX Battle": Everhood2LocationData(BATTLE_LOCATION_START + 94, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),

    "Processor Gate Battle": Everhood2LocationData(BATTLE_LOCATION_START + 95, "Smega Console", LocationType.major_battle | LocationType.pre_dragon_doors, "250xp"),
    "Processor INT Battle": Everhood2LocationData(BATTLE_LOCATION_START + 96, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "Processor FLOAT Battle": Everhood2LocationData(BATTLE_LOCATION_START + 97, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "Processor MATRIX Battle": Everhood2LocationData(BATTLE_LOCATION_START + 98, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "Processor BOOL Battle": Everhood2LocationData(BATTLE_LOCATION_START + 99, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "Processor CHAR Battle": Everhood2LocationData(BATTLE_LOCATION_START + 100, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp"),
    "Processor WHILE x2 Battle": Everhood2LocationData(BATTLE_LOCATION_START + 101, "Smega Console", LocationType.trash_battle | LocationType.pre_dragon_doors, "128xp"),
    "Corrupt Irvine Battle": Everhood2LocationData(BATTLE_LOCATION_START + 102, "Smega Console", LocationType.major_battle | LocationType.pre_dragon_doors, "1200xp"),
    
    # "Rock Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 103, "Death Mountain", LocationType.trash_battle | LocationType.post_dragon, "200xp"),
    # "Rock Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 104, "Death Mountain", LocationType.trash_battle | LocationType.post_dragon, "200xp"),
    # "Mimic Chest Battle": Everhood2LocationData(BATTLE_LOCATION_START + 105, "Death Mountain", LocationType.trash_battle | LocationType.post_dragon, "250xp"),
    # "Mimic Apple Battle": Everhood2LocationData(BATTLE_LOCATION_START + 106, "Death Mountain", LocationType.trash_battle | LocationType.post_dragon, "300xp"),
    # "Harpy Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 107, "Death Mountain", LocationType.trash_battle | LocationType.post_dragon, "250xp"),
    # "Zombie Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 108, "Death Mountain", LocationType.trash_battle | LocationType.post_dragon, "300xp"),
    # "Zombie Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 109, "Death Mountain", LocationType.trash_battle | LocationType.post_dragon, "300xp"),
    # "Zombie Battle 3": Everhood2LocationData(BATTLE_LOCATION_START + 110, "Death Mountain", LocationType.trash_battle | LocationType.post_dragon, "300xp"),
    # "Rock Battle 3": Everhood2LocationData(BATTLE_LOCATION_START + 111, "Death Mountain", LocationType.trash_battle | LocationType.post_dragon, "200xp"),
    # "Harpy Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 112, "Death Mountain", LocationType.trash_battle | LocationType.post_dragon, "250xp"),
    # "Crab Machine Battle": Everhood2LocationData(BATTLE_LOCATION_START + 113, "Death Mountain", LocationType.major_battle | LocationType.post_dragon, "1000xp"),
    
    # "Dmitri Battle": Everhood2LocationData(BATTLE_LOCATION_START + 114, "Tutorial Spaceship", LocationType.major_battle | LocationType.post_dragon, "650xp"),
    
    # "Yellow Battle": Everhood2LocationData(BATTLE_LOCATION_START + 115, "Everhood 1", LocationType.major_battle | LocationType.post_dragon, "800xp"),
    # "Cursed Castle Battle": Everhood2LocationData(BATTLE_LOCATION_START + 116, "Everhood 1", LocationType.major_battle | LocationType.post_dragon, "800xp"),
    # "Light Being Battle": Everhood2LocationData(BATTLE_LOCATION_START + 117, "Everhood 1", LocationType.unique_battle | LocationType.post_dragon, "600xp"),
    # "Slot Machine Battle": Everhood2LocationData(BATTLE_LOCATION_START + 118, "Everhood 1", LocationType.unique_battle | LocationType.post_dragon, "500xp"), #Todo: Keep skippable?
    
    # "Judge Creation Battle": Everhood2LocationData(BATTLE_LOCATION_START + 119, "Deep Sea", LocationType.major_battle | LocationType.post_dragon, "0xp"),
    
    # "Jean D'Arc Battle": Everhood2LocationData(BATTLE_LOCATION_START + 120, "Colosseum", LocationType.major_battle | LocationType.colosseum, "350xp"),
    # "Molly Battle": Everhood2LocationData(BATTLE_LOCATION_START + 121, "Colosseum", LocationType.major_battle | LocationType.colosseum, "888xp"),
    # "RAM FOR LOOP Battle": Everhood2LocationData(BATTLE_LOCATION_START + 122, "Colosseum", LocationType.major_battle | LocationType.colosseum, "500xp"),
    # "Dragon 3 Battle": Everhood2LocationData(BATTLE_LOCATION_START + 123, "Colosseum", LocationType.major_battle | LocationType.colosseum, "0xp"),
    # "Mushroom House Battle": Everhood2LocationData(BATTLE_LOCATION_START + 124, "Colosseum", LocationType.major_battle | LocationType.colosseum | LocationType.post_game, "200xp"),

    # "Bobo Battle": Everhood2LocationData(BATTLE_LOCATION_START + 125, "Pandemonium", LocationType.major_battle | LocationType.post_dragon, "0xp"),
    # "Shade Demon Battle": Everhood2LocationData(BATTLE_LOCATION_START + 126, "Pandemonium", LocationType.major_battle | LocationType.post_dragon, "0xp"),
    # "Black Hole Battle": Everhood2LocationData(BATTLE_LOCATION_START + 127, "Pandemonium", LocationType.major_battle | LocationType.post_dragon, "0xp"),

    # "Void Harpy Battle 1": Everhood2LocationData(BATTLE_LOCATION_START + 128, "Riley's Fortress", LocationType.trash_battle | LocationType.post_dragon, "0xp"),
    # "Void Harpy Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 129, "Riley's Fortress", LocationType.trash_battle | LocationType.post_dragon, "0xp"),
    # "Void Harpy Battle 3": Everhood2LocationData(BATTLE_LOCATION_START + 130, "Riley's Fortress", LocationType.trash_battle | LocationType.post_dragon, "0xp"),
    # "Void Harpy Battle 4": Everhood2LocationData(BATTLE_LOCATION_START + 131, "Riley's Fortress", LocationType.trash_battle | LocationType.post_dragon, "0xp"),
    # "Void Harpy Battle 5": Everhood2LocationData(BATTLE_LOCATION_START + 132, "Riley's Fortress", LocationType.trash_battle | LocationType.post_dragon, "0xp"),
    # "Evren Battle": Everhood2LocationData(BATTLE_LOCATION_START + 133, "Riley's Fortress", LocationType.major_battle | LocationType.post_dragon, "0xp"),
    # "Riley Battle": Everhood2LocationData(BATTLE_LOCATION_START + 134, "Riley's Fortress", LocationType.major_battle | LocationType.post_dragon, "0xp"),
    
    # "Dragon Battle": Everhood2LocationData(BATTLE_LOCATION_START + 135, "Hall of Con", LocationType.major_battle | LocationType.post_dragon, "0xp"),
    # "Post Credits Shade Battle": Everhood2LocationData(BATTLE_LOCATION_START + 136, "Riley's Fortress", LocationType.major_battle | LocationType.post_game, "0xp"),
}

all_locations: ChainMap[str, Everhood2LocationData] = ChainMap(item_locations, battle_locations)
