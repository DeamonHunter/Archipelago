from typing import Dict, NamedTuple, Optional
from enum import IntFlag, auto
from BaseClasses import Location
from collections import ChainMap


ITEM_LOCATION_START = 100
BATTLE_LOCATION_START = 500


class LocationType(IntFlag):
    item = auto()
    cosmetic = auto()
    major_battle = auto()
    unique_battle = auto()
    trash_battle = auto()
    
    hillbert = auto()
    colosseum = auto()
    pre_dragon_doors = auto()
    post_game = auto()
    
    act_2 = auto()
    act_3 = auto()


class Color(IntFlag):
    blue = auto()
    red = auto()
    green = auto()
    yellow = auto()
    brown = auto()
    purple = auto()
    orange = auto()


class Everhood2LocationData(NamedTuple):
    code: Optional[int]
    region: str
    type: LocationType
    item_name: str
    color: Color = 0


class Everhood2EventData(NamedTuple):
    region: str
    type: LocationType


class Everhood2Location(Location):
    game: str = "Everhood 2"


item_locations: Dict[str, Everhood2LocationData] = {    
    # Guarded by Pirahna
    "Neon Jungle Chest Section 1 South East": Everhood2LocationData(ITEM_LOCATION_START + 0, "Neon City - Pre Homonculus", LocationType.item, "50xp", Color.blue | Color.green),
    "Neon Jungle Chest Section 1 North West": Everhood2LocationData(ITEM_LOCATION_START + 1, "Neon City - Pre Homonculus", LocationType.item, "75xp"),
    "Neon Jungle Chest Section 2 North West": Everhood2LocationData(ITEM_LOCATION_START + 2, "Neon City - Post Homonculus", LocationType.item, "50xp"),
    "Neon Jungle Chest Section 2 South East": Everhood2LocationData(ITEM_LOCATION_START + 3, "Neon City - Post Homonculus", LocationType.item, "75xp"),
    "Neon Jungle Chest Section 3 West": Everhood2LocationData(ITEM_LOCATION_START + 4, "Neon City - Post Cowgirl Homonculus", LocationType.item, "100xp"),
    "Neon Jungle Chest Section 3 East": Everhood2LocationData(ITEM_LOCATION_START + 5, "Neon City - Post Cowgirl Homonculus", LocationType.item, "0xp"),
    "Neon Jungle Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 6, "Neon City - Post Cowgirl Homonculus", LocationType.item, "Power Gem"),
    
    "Anime Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 7, "Neon City - Pre Homonculus", LocationType.cosmetic, "Anime Hairstyle Cosmetic"),
    "Mage Hat Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 8, "Neon City - Pre Homonculus", LocationType.cosmetic, "Mage Hat Cosmetic"),
    "Wild Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 9, "Neon City - Pre Homonculus", LocationType.cosmetic, "Wild Hairstyle Cosmetic"),
    "Backslick Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 10, "Neon City - Pre Homonculus", LocationType.cosmetic, "Backslick Hairstyle Cosmetic"),
    "Stylish Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 11, "Neon City - Pre Homonculus", LocationType.cosmetic, "Stylish Hairstyle Cosmetic"),
    "Natural Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 12, "Neon City - Pre Homonculus", LocationType.cosmetic, "Natural Hairstyle Cosmetic"), 
    "Afro Hairstyle Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 13, "Neon City - Pre Homonculus", LocationType.cosmetic, "Afro Cosmetic"),
    
    "Eternal War - Chest After Melon": Everhood2LocationData(ITEM_LOCATION_START + 14, "Eternal War - Bridge And Dungeon", LocationType.item, "100xp"),
    "Hotdog Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 15, "Eternal War - Bridge And Dungeon", LocationType.cosmetic, "Hotdog Cosmetic", Color.green | Color.purple | Color.yellow),
    "Eternal War - Chest Behind Chili": Everhood2LocationData(ITEM_LOCATION_START + 16, "Eternal War - Bridge And Dungeon", LocationType.item, "50xp", Color.green | Color.purple | Color.yellow),
    "Eternal War - Chest Behind Leek": Everhood2LocationData(ITEM_LOCATION_START + 17, "Eternal War - Tomato Rampages", LocationType.item, "75xp", Color.green | Color.purple),
    "Eternal War - Chest Behind Bell Pepper": Everhood2LocationData(ITEM_LOCATION_START + 18, "Eternal War - Tomato Rampages", LocationType.item, "50xp", Color.blue),
    "Eternal War - Final Chest": Everhood2LocationData(ITEM_LOCATION_START + 19, "Eternal War - Post Win", LocationType.item, "50xp"),
    
    "Eternal War - Dungeon Chest": Everhood2LocationData(ITEM_LOCATION_START + 20, "Eternal War - Bridge And Dungeon", LocationType.item, "50xp"),
    "Eternal War - Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 21, "Eternal War - Bridge And Dungeon", LocationType.item, "Power Gem"),
    
    "Marzian Era 0 - Mines Chest": Everhood2LocationData(ITEM_LOCATION_START + 22, "Marzian Era 0 - Mines B", LocationType.item, "50xp"),
    "Marzian Era 0 - Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 23, "Marzian Era 0 - Mines C", LocationType.item, "Power Gem"),
    
    "Marzian Era 0 - Mining Base Chest": Everhood2LocationData(ITEM_LOCATION_START + 24, "Marzian Era 0 - Base C", LocationType.item, "Crimson Bandanna"),
    "Red Bandana Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 25, "Marzian Era 0 - Base C", LocationType.cosmetic, "Red Bandana Cosmetic"),

    "Floor 23 Key": Everhood2LocationData(ITEM_LOCATION_START + 26, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "Floor 23 Key"),
    "Floor 23 Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 27, "Floor 23 - Rewards", LocationType.item | LocationType.hillbert, "100xp"),
    "Cat Ears": Everhood2LocationData(ITEM_LOCATION_START + 28, "Floor 23 - Rewards", LocationType.cosmetic | LocationType.hillbert, "Cat Ears Cosmetic"),
    "Cat Ears Bald": Everhood2LocationData(ITEM_LOCATION_START + 29, "Floor 23 - Rewards", LocationType.cosmetic | LocationType.hillbert, "Cat Ears Bald Cosmetic"),
    "Gold Key": Everhood2LocationData(ITEM_LOCATION_START + 30, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "Gold Key"),
    "Floor Gold Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 31, "Floor Gold - Post Bobo", LocationType.item | LocationType.hillbert, "50xp"),
    "Oingo Boingo": Everhood2LocationData(ITEM_LOCATION_START + 32, "Floor Gold - Post Bobo", LocationType.cosmetic | LocationType.hillbert, "Oingo Boingo Cosmetic"),

    "Floor 23 Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 33, "Floor 23", LocationType.item | LocationType.hillbert, "50xp"),
    "Floor 23 Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 34, "Floor 23", LocationType.item | LocationType.hillbert, "50xp"),
    "Floor 23 Smega Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 35, "Floor 23 - Smega", LocationType.item | LocationType.hillbert, "50xp", Color.red | Color.blue),
    
    "Floor Gold Chest": Everhood2LocationData(ITEM_LOCATION_START + 36, "Floor Gold", LocationType.item | LocationType.hillbert, "50xp"),
    "Green Key": Everhood2LocationData(ITEM_LOCATION_START + 37, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "Green Key"),
    
    "Stopwatch Artifact": Everhood2LocationData(ITEM_LOCATION_START + 39, "Infinity Hub", LocationType.item, "Stopwatch"), # Technically in tutorial area, but not modelling that.
    
    "Floor Green Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 41, "Floor Green", LocationType.item | LocationType.hillbert, "Power Gem"),
    "Pinecone Key": Everhood2LocationData(ITEM_LOCATION_START + 42, "Hillbert Hotel", LocationType.item | LocationType.hillbert, "Pinecone Key"),
    "Floor Pinecone Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 43, "Floor Pinecone - Post Squirrels", LocationType.item | LocationType.hillbert, "Power Gem"),
    "Reindeer Skull": Everhood2LocationData(ITEM_LOCATION_START + 44, "Floor Pinecone - Post Squirrels", LocationType.cosmetic | LocationType.hillbert, "Reindeer Skull Cosmetic"),
    # "Floor Omega Key": Everhood2LocationData(ITEM_LOCATION_START + 45, "Hillbert Hotel", LocationType.item | LocationType.hillbert | LocationType.post_dragon, "Omega Key"),
    # "Floor Omega Reward Chest": Everhood2LocationData(ITEM_LOCATION_START + 46, "Hillbert Hotel", LocationType.item | LocationType.hillbert | LocationType.post_dragon, "Power Gem"),
    # "Jester Hat": Everhood2LocationData(ITEM_LOCATION_START + 47, "Hillbert Hotel", LocationType.cosmetic | LocationType.hillbert | LocationType.post_dragon, "Jester Hat Cosmetic"),
    
    "Floor Pinecone Chest": Everhood2LocationData(ITEM_LOCATION_START + 48, "Floor Pinecone - Post Squirrels", LocationType.item | LocationType.hillbert, "50xp"),
    
    # "Marzian Era 3000 Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 49, "Marzian Era 3000", LocationType.item | LocationType.post_dragon, "100xp"),
    # "Marzian Era 3000 Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 50, "Marzian Era 3000", LocationType.item | LocationType.post_dragon, "50xp"),

    # "Marzian Era 4000 Chest": Everhood2LocationData(ITEM_LOCATION_START + 51, "Marzian Era 4000", LocationType.item | LocationType.post_dragon, "Power Gem"),

    "Sun Insignia": Everhood2LocationData(ITEM_LOCATION_START + 52, "Mushroom Bureau - Sun", LocationType.item | LocationType.act_2, "Sun Emblem", Color.yellow | Color.blue | Color.brown),
    "Mushroom Bureau Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 53, "Mushroom Bureau - Moon", LocationType.item | LocationType.act_2, "Power Gem"),
    "Moon Insignia": Everhood2LocationData(ITEM_LOCATION_START + 54, "Mushroom Bureau - Gauntlet 2", LocationType.item | LocationType.act_2, "Moon Emblem", Color.blue | Color.orange),
    "Mushroom Bureau Death Coin": Everhood2LocationData(ITEM_LOCATION_START + 55, "Mushroom Bureau - Finale", LocationType.item | LocationType.act_2, "Death Coin"),
    "Mushroom Hat": Everhood2LocationData(ITEM_LOCATION_START + 116, "Mushroom Bureau - Moon", LocationType.item | LocationType.act_2 | LocationType.cosmetic, "Mushroom Hat Cosmetic"),

    # "Duality Artifact": Everhood2LocationData(ITEM_LOCATION_START + 56, "Lucy's Room", LocationType.item | LocationType.post_dragon, "Duality"),
    
    # Todo: Do we replace this with a progressive green key?
    # "Crystal Key": Everhood2LocationData(ITEM_LOCATION_START + 57, "Sam's Room", LocationType.item | LocationType.post_dragon, "Crystal Key"),

    # Todo: Determine how soul weapons are placed.
    # "Marzian Soul Weapon": Everhood2LocationData(ITEM_LOCATION_START + 58, "Marzian Era 4000", LocationType.item | LocationType.post_dragon, "Soul Weapon"),

    "Lab Entrance Chest": Everhood2LocationData(ITEM_LOCATION_START + 59, "Lab - Pre Puzzle", LocationType.item | LocationType.pre_dragon_doors, "35xp"),
    "Clover Artifact": Everhood2LocationData(ITEM_LOCATION_START + 60, "Lab - Pre Puzzle", LocationType.item | LocationType.pre_dragon_doors, "Clover"),
    "Lab Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 61, "Lab - Pre Puzzle", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),

    # "Floor Omega Chest": Everhood2LocationData(ITEM_LOCATION_START + 62, "Floor Omega", LocationType.item | LocationType.post_dragon, "Power Gem"),

    "Liminal Room Chest 1": Everhood2LocationData(ITEM_LOCATION_START + 63, "Liminal Room", LocationType.item | LocationType.act_2, "Power Gem"), 
    "Liminal Room Chest 2": Everhood2LocationData(ITEM_LOCATION_START + 64, "Liminal Room", LocationType.item | LocationType.act_2, "Power Gem"),

    "Smega Console - 'D' Chest": Everhood2LocationData(ITEM_LOCATION_START + 65, "Smega Console - Motherboard A", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - Chest Before Riley": Everhood2LocationData(ITEM_LOCATION_START + 66, "Smega Console - Motherboard A", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - Chest Behind Motherboard Bool": Everhood2LocationData(ITEM_LOCATION_START + 67, "Smega Console - Motherboard B", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"), #Has complex color rule
    "Smega Console - Audio Chest": Everhood2LocationData(ITEM_LOCATION_START + 68, "Smega Console - Motherboard B", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Gas Mask Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 69, "Smega Console - Doctor Dump", LocationType.cosmetic | LocationType.pre_dragon_doors, "Gas Mask Cosmetic"),
    "Doctor Dump Power Gem": Everhood2LocationData(ITEM_LOCATION_START + 70, "Smega Console - Doctor Dump", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console - RAM N Chest D/E": Everhood2LocationData(ITEM_LOCATION_START + 71, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - RAM SE Chest by Dunkey": Everhood2LocationData(ITEM_LOCATION_START + 72, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "100xp"),
    "Smega Console - RAM SE Chest A/B": Everhood2LocationData(ITEM_LOCATION_START + 73, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - Ram SW Northern Chest": Everhood2LocationData(ITEM_LOCATION_START + 74, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console - RAM N Chest F": Everhood2LocationData(ITEM_LOCATION_START + 75, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - RAM SE Chest A/Y": Everhood2LocationData(ITEM_LOCATION_START + 76, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console - RAM SE Chest Y/C": Everhood2LocationData(ITEM_LOCATION_START + 77, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - RAM N Chest F/C": Everhood2LocationData(ITEM_LOCATION_START + 78, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console - Ram SW Southern Chest": Everhood2LocationData(ITEM_LOCATION_START + 79, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - Ram SW Center Chest": Everhood2LocationData(ITEM_LOCATION_START + 80, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - RAM SE Chest B/F": Everhood2LocationData(ITEM_LOCATION_START + 81, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console - Ram SW Eastern Chest": Everhood2LocationData(ITEM_LOCATION_START + 82, "Smega Console - RAM", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - Maze Chest Behind Matrix": Everhood2LocationData(ITEM_LOCATION_START + 83, "Smega Console - Processor B", LocationType.item | LocationType.pre_dragon_doors, "Power Gem", Color.red | Color.blue | Color.purple),
    "Smega Console - Maze Chest East": Everhood2LocationData(ITEM_LOCATION_START + 84, "Smega Console - Processor B", LocationType.item | LocationType.pre_dragon_doors, "Power Gem"),
    "Smega Console - Post Maze Chest": Everhood2LocationData(ITEM_LOCATION_START + 85, "Smega Console - Processor B", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - Chest After Processor Int": Everhood2LocationData(ITEM_LOCATION_START + 86, "Smega Console - Processor B", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    "Smega Console - Maze Chest South": Everhood2LocationData(ITEM_LOCATION_START + 87, "Smega Console - Processor B", LocationType.item | LocationType.pre_dragon_doors, "50xp"),
    
    "Death Mountain Chest Near Entrance": Everhood2LocationData(ITEM_LOCATION_START + 88, "Death Mountain", LocationType.item | LocationType.act_2, "50xp"),
    "Death Mountain Chest Past Blockade": Everhood2LocationData(ITEM_LOCATION_START + 89, "Death Mountain", LocationType.item | LocationType.act_2, "Power Gem"),
    "Death Mountain Chest Near Rock Fall": Everhood2LocationData(ITEM_LOCATION_START + 90, "Death Mountain", LocationType.item | LocationType.act_2, "Power Gem"),
    "Death Mountain Chest Behind Harpy": Everhood2LocationData(ITEM_LOCATION_START + 91, "Death Mountain", LocationType.item | LocationType.act_2, "50xp"), # Harpy spams white notes
    "Death Mountain Chest Overlooking Cliff": Everhood2LocationData(ITEM_LOCATION_START + 92, "Death Mountain", LocationType.item | LocationType.act_2, "50xp"),
    "Death Mountain Chest Near Harpy Village": Everhood2LocationData(ITEM_LOCATION_START + 93, "Death Mountain", LocationType.item | LocationType.act_2, "50xp"),
    "Death Mountain Scholar Puzzle Chest": Everhood2LocationData(ITEM_LOCATION_START + 94, "Death Mountain", LocationType.item | LocationType.act_2, "Death Coin"),
    "Death Mountain King Gordo Reward": Everhood2LocationData(ITEM_LOCATION_START + 95, "Death Mountain", LocationType.item | LocationType.act_2, "Death Coin"),

    "V.I.P. Ticket": Everhood2LocationData(ITEM_LOCATION_START + 96, "Everhood 1 - Intro", LocationType.item | LocationType.act_2, "V.I.P. Ticket"),
    # Todo: This is a blocker that may not want to be added?
    # "Long Plank": Everhood2LocationData(ITEM_LOCATION_START + 97, "Everhood 1 - Intro", LocationType.item | LocationType.post_dragon, "Long Plank"),
    "Yellow Mask": Everhood2LocationData(ITEM_LOCATION_START + 98, "Everhood 1 - Post Yellow", LocationType.item | LocationType.act_2, "Yellow Mask"),
    "Everhood 1 Death Coin": Everhood2LocationData(ITEM_LOCATION_START + 99, "Everhood 1 - Post Castle", LocationType.item | LocationType.act_2, "Death Coin"),
    "Light Being Soul Weapon": Everhood2LocationData(ITEM_LOCATION_START + 100, "Everhood 1 - Post Castle", LocationType.item | LocationType.act_2, "Soul Weapon"),

    # "Colosseum Reward 1": Everhood2LocationData(ITEM_LOCATION_START + 101, "Colosseum", LocationType.item | LocationType.colosseum, "Power Gem"),
    # "Knight Helmet Cosmetic": Everhood2LocationData(ITEM_LOCATION_START + 102, "Colosseum", LocationType.cosmetic | LocationType.colosseum, "Knight Helmet Cosmetic"),
    # "Colosseum Reward 2": Everhood2LocationData(ITEM_LOCATION_START + 103, "Colosseum", LocationType.item | LocationType.colosseum, "Death Coin"),
    # "Colosseum Reward 3": Everhood2LocationData(ITEM_LOCATION_START + 104, "Colosseum", LocationType.item | LocationType.colosseum, "Power Gem x2"),
    # "Colosseum Reward 4": Everhood2LocationData(ITEM_LOCATION_START + 105, "Colosseum", LocationType.item | LocationType.colosseum, "Power Gem x3"),
    # "Colosseum Reward 5": Everhood2LocationData(ITEM_LOCATION_START + 106, "Colosseum", LocationType.item | LocationType.colosseum | LocationType.post_game, "Power Gem x2"),
    # "Colosseum Reward 6": Everhood2LocationData(ITEM_LOCATION_START + 107, "Colosseum", LocationType.item | LocationType.colosseum | LocationType.post_game, "Power Gem x2"),

    # "Pandemonium Chest": Everhood2LocationData(ITEM_LOCATION_START + 108, "Colosseum", LocationType.item | LocationType.post_dragon, "Power Gem"),
    # "Torment Room Chest": Everhood2LocationData(ITEM_LOCATION_START + 109, "Colosseum", LocationType.item | LocationType.post_dragon, "Power Gem"),
    
    "Katana": Everhood2LocationData(ITEM_LOCATION_START + 110, "Lab - Pre Puzzle", LocationType.item | LocationType.pre_dragon_doors, "Katana"), #Technically requires white
    "Dragon Soul Weapon": Everhood2LocationData(ITEM_LOCATION_START + 111, "Time Hub", LocationType.item | LocationType.act_2, "Soul Weapon"),
    "Pet the Orange Cat": Everhood2LocationData(ITEM_LOCATION_START + 112, "Home Town", LocationType.item | LocationType.pre_dragon_doors, "5xp"),
    "Pet the Grey Cat": Everhood2LocationData(ITEM_LOCATION_START + 113, "Home Town", LocationType.item | LocationType.pre_dragon_doors, "5xp"),
    "Pet the Black Cat": Everhood2LocationData(ITEM_LOCATION_START + 114, "Home Town", LocationType.item | LocationType.pre_dragon_doors, "-2xp"),
    "Bead Braclet": Everhood2LocationData(ITEM_LOCATION_START + 115, "Home Town", LocationType.item | LocationType.pre_dragon_doors, "Bead Braclet"),
}

battle_locations: Dict[str, Everhood2LocationData] = {
    # Starting Battle
    "Raven Tutorial Battle": Everhood2LocationData(BATTLE_LOCATION_START + 0, "Tutorial Hub", LocationType.major_battle, "0xp"),
    # Pre Neon City
    "Spring Head Battle Before City": Everhood2LocationData(BATTLE_LOCATION_START + 1, "Neon City - Pre Homonculus", LocationType.trash_battle, "20xp", Color.red | Color.green),
    # Neon Jungle Room 1
    "Spring Head Battle Section 1 Right": Everhood2LocationData(BATTLE_LOCATION_START + 2, "Neon City - Pre Homonculus", LocationType.trash_battle, "20xp", Color.red | Color.green),
    "Spring Head Battle Section 1 Left": Everhood2LocationData(BATTLE_LOCATION_START + 3, "Neon City - Pre Homonculus", LocationType.trash_battle, "20xp", Color.red | Color.green),
    "Double Spring Head Section 1": Everhood2LocationData(BATTLE_LOCATION_START + 4, "Neon City - Pre Homonculus", LocationType.trash_battle, "40xp", Color.red | Color.green),
    "Dark Pirahna Section 1 Chest Protector": Everhood2LocationData(BATTLE_LOCATION_START + 5, "Neon City - Pre Homonculus", LocationType.trash_battle, "30xp", Color.blue | Color.green),
    "Dark Pirahna Section 1 Exit": Everhood2LocationData(BATTLE_LOCATION_START + 6, "Neon City - Pre Homonculus", LocationType.trash_battle, "30xp", Color.blue | Color.green),
    # Neon Jungle Room 2
    "Homonculus Battle": Everhood2LocationData(BATTLE_LOCATION_START + 7, "Neon City - Pre Homonculus", LocationType.major_battle, "35xp", Color.green | Color.blue | Color.purple),
    "Spring Head Battle Section 2 Middle": Everhood2LocationData(BATTLE_LOCATION_START + 8, "Neon City - Post Homonculus", LocationType.trash_battle, "20xp", Color.red | Color.green),
    "Spring Head Battle Section 2 North": Everhood2LocationData(BATTLE_LOCATION_START + 9, "Neon City - Post Homonculus", LocationType.trash_battle, "20xp", Color.red | Color.green),
    "Spring Head Battle Section 2 South": Everhood2LocationData(BATTLE_LOCATION_START + 10, "Neon City - Post Homonculus", LocationType.trash_battle, "20xp", Color.red | Color.green),
    "Neon String Section 2": Everhood2LocationData(BATTLE_LOCATION_START + 11, "Neon City - Post Homonculus", LocationType.trash_battle, "50xp", Color.green | Color.red),
    "Dark Pirahna Section 2": Everhood2LocationData(BATTLE_LOCATION_START + 12, "Neon City - Post Homonculus", LocationType.trash_battle, "30xp", Color.blue | Color.green),
    # Neon Jungle Room 3
    "Cowgirl Homonculus Battle": Everhood2LocationData(BATTLE_LOCATION_START + 13, "Neon City - Post Homonculus", LocationType.major_battle, "36xp", Color.green | Color.blue),
    "Double Spring Head Battle Section 3": Everhood2LocationData(BATTLE_LOCATION_START + 14, "Neon City - Post Cowgirl Homonculus", LocationType.trash_battle, "40xp", Color.red | Color.green),
    "Double Dark Pirahna Battle": Everhood2LocationData(BATTLE_LOCATION_START + 15, "Neon City - Post Cowgirl Homonculus", LocationType.trash_battle, "60xp", Color.blue | Color.green),
    "Neon String Section 3": Everhood2LocationData(BATTLE_LOCATION_START + 16, "Neon City - Post Cowgirl Homonculus", LocationType.trash_battle, "50xp", Color.green | Color.red),
    
    # Todo: Abyss doesn't have a proper end
    
    # Marzian Era 0 Mines
    "Hyena Battle Screech": Everhood2LocationData(BATTLE_LOCATION_START + 18, "Marzian Era 0 - Mines A", LocationType.trash_battle, "25xp", Color.green | Color.blue),
    "Hyena Battle Warcry": Everhood2LocationData(BATTLE_LOCATION_START + 19, "Marzian Era 0 - Mines B", LocationType.trash_battle, "25xp", Color.green | Color.blue),
    "Shark Battle Bloodnose": Everhood2LocationData(BATTLE_LOCATION_START + 20, "Marzian Era 0 - Mines B", LocationType.trash_battle, "25xp", Color.green | Color.orange),
    "Howler & Razor Battle": Everhood2LocationData(BATTLE_LOCATION_START + 21, "Marzian Era 0 - Mines B", LocationType.major_battle, "50xp"), # Has custom color rule
    "Feugo Battle": Everhood2LocationData(BATTLE_LOCATION_START + 22, "Marzian Era 0 - Mines C", LocationType.major_battle, "100xp", Color.green | Color.blue | Color.red), #Also has a single purple

    # Marzian Era 0 Base
    "Insect Abomination Battle": Everhood2LocationData(BATTLE_LOCATION_START + 23, "Marzian Era 0 - Base A", LocationType.major_battle, "50xp", Color.red | Color.green),
    "Anxious Chase Battle": Everhood2LocationData(BATTLE_LOCATION_START + 24, "Marzian Era 0 - Base B", LocationType.major_battle, "2xp", Color.green),
    "Howler & Razor & Maggot Battle": Everhood2LocationData(BATTLE_LOCATION_START + 25, "Marzian Era 0 - Base C", LocationType.trash_battle, "75xp"), # Has custom color rule
    "Dimension Master Battle": Everhood2LocationData(BATTLE_LOCATION_START + 26, "Marzian Era 0 - Base D", LocationType.major_battle, "200xp", Color.green | Color.blue | Color.red),
    
    "Dimension Portal Battle": Everhood2LocationData(BATTLE_LOCATION_START + 27, "Marzian Era 1000", LocationType.major_battle, "400xp", Color.green | Color.blue | Color.red),
    "Blue Stonegrunt Battle": Everhood2LocationData(BATTLE_LOCATION_START + 28, "Marzian Era 2000", LocationType.major_battle, "150xp", Color.green | Color.blue ),

    # Eternal War Desert
    "Red Onion Battle": Everhood2LocationData(BATTLE_LOCATION_START + 29, "Eternal War - Tomato Rampages", LocationType.trash_battle, "15xp", Color.red | Color.green | Color.blue),
    "Leek Battle": Everhood2LocationData(BATTLE_LOCATION_START + 30, "Eternal War - Tomato Rampages", LocationType.unique_battle, "76xp", Color.green | Color.purple),
    "Bro-ccoli": Everhood2LocationData(BATTLE_LOCATION_START + 31, "Eternal War - Tomato Rampages", LocationType.unique_battle, "76xp", Color.blue | Color.brown),
    "Bell Pepper Battle": Everhood2LocationData(BATTLE_LOCATION_START + 32, "Eternal War - Tomato Rampages", LocationType.unique_battle, "100xp", Color.blue),
    "Tomato Rush Lower Left Battle": Everhood2LocationData(BATTLE_LOCATION_START + 33, "Eternal War - Tomato Rampages", LocationType.trash_battle, "25xp", Color.red | Color.orange | Color.blue | Color.green), # White.
    "Tomato Rush Lower Middle Battle": Everhood2LocationData(BATTLE_LOCATION_START + 34, "Eternal War - Tomato Rampages", LocationType.trash_battle, "25xp", Color.red | Color.orange | Color.blue | Color.green), # White.
    "Tomato Rush Lower Right Battle": Everhood2LocationData(BATTLE_LOCATION_START + 35, "Eternal War - Tomato Rampages", LocationType.trash_battle, "25xp", Color.red | Color.orange | Color.blue | Color.green), # White.
    "Tomato Rush Upper Left Battle": Everhood2LocationData(BATTLE_LOCATION_START + 36, "Eternal War - Tomato Rampages", LocationType.trash_battle, "25xp", Color.red | Color.orange | Color.blue | Color.green), # White.
    "Tomato Rush Upper Middle Battle": Everhood2LocationData(BATTLE_LOCATION_START + 37, "Eternal War - Tomato Rampages", LocationType.trash_battle, "25xp", Color.red | Color.orange | Color.blue | Color.green), # White.
    "Tomato Rush Upper Right Battle": Everhood2LocationData(BATTLE_LOCATION_START + 38, "Eternal War - Tomato Rampages", LocationType.trash_battle, "25xp", Color.red | Color.orange | Color.blue | Color.green), # White.
    "Melon Battle": Everhood2LocationData(BATTLE_LOCATION_START + 39, "Eternal War - Tomato Rampages", LocationType.major_battle, "100xp", Color.green | Color.red | Color.blue), #Yellow, Purple
    "Chili Battle": Everhood2LocationData(BATTLE_LOCATION_START + 40, "Eternal War - Bridge And Dungeon", LocationType.unique_battle, "15xp", Color.green | Color.purple | Color.yellow), #Orange also appears in phase 2, but can't beat phase 1

    # Eternal War Castle
    "Capsicum Battle": Everhood2LocationData(BATTLE_LOCATION_START + 41, "Eternal War - Bridge And Dungeon", LocationType.major_battle, "70xp", Color.purple),
    "Carrot Mage Battle": Everhood2LocationData(BATTLE_LOCATION_START + 42, "Eternal War - Tournament A", LocationType.major_battle, "45xp", Color.purple | Color.green | Color.red | Color.yellow),
    "Juice Master#4671 Battle": Everhood2LocationData(BATTLE_LOCATION_START + 43, "Eternal War - Tournament B", LocationType.major_battle, "150xp", Color.green | Color.blue), # Red Waves which maybe are painful to get in a good number
    
    # Hillbert Hotel Fights
    # Angry Wizard Todo
    "Hillbert Processor Int Battle": Everhood2LocationData(BATTLE_LOCATION_START + 45, "Floor 23 - Smega", LocationType.unique_battle | LocationType.hillbert, "64xp", Color.blue | Color.red),
    "Rasputin Battle": Everhood2LocationData(BATTLE_LOCATION_START + 46, "Floor 23", LocationType.major_battle | LocationType.hillbert, "100xp", Color.red | Color.green | Color.blue), # Other colors are used, but these are the only ones in the final phase
    "Bobo (Drunk) Battle": Everhood2LocationData(BATTLE_LOCATION_START + 47, "Floor Gold", LocationType.major_battle | LocationType.hillbert, "80xp"), #Red, Green, Blue, Brown but has a LOT of white
    
    "Squirrels Battle": Everhood2LocationData(BATTLE_LOCATION_START + 48, "Floor Pinecone", LocationType.major_battle | LocationType.hillbert, "400xp", Color.green | Color.purple | Color.brown),
    
    "Opus & Screech Battle": Everhood2LocationData(BATTLE_LOCATION_START + 50, "Marzian Era 0 - Base C", LocationType.trash_battle, "80xp"), # Has Custom Color Rule

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

    "Brown Slow Mushroom Sun Battle": Everhood2LocationData(BATTLE_LOCATION_START + 63, "Mushroom Bureau - Sun", LocationType.major_battle | LocationType.act_2, "50xp", Color.yellow | Color.blue | Color.brown), # Todo: Are both mushroom fights the same?
    "Hydra Mushroom Dance Room Battle": Everhood2LocationData(BATTLE_LOCATION_START + 64, "Mushroom Bureau - Moon", LocationType.unique_battle | LocationType.act_2, "50xp", Color.orange),
    "Smelly Gas Mushroom Dance Room Battle": Everhood2LocationData(BATTLE_LOCATION_START + 65, "Mushroom Bureau - Moon", LocationType.unique_battle | LocationType.act_2, "50xp", Color.blue | Color.yellow),
    "Smelly Gas Mushroom Gauntlet Battle": Everhood2LocationData(BATTLE_LOCATION_START + 137, "Mushroom Bureau - Gauntlet 1", LocationType.unique_battle | LocationType.act_2, "50xp", Color.blue | Color.yellow),
    "Brown Slow Mushroom Gauntlet Battle": Everhood2LocationData(BATTLE_LOCATION_START + 66, "Mushroom Bureau - Gauntlet 2", LocationType.unique_battle | LocationType.act_2, "50xp", Color.yellow | Color.blue | Color.brown),
    "Sun Knight Gauntlet Battle": Everhood2LocationData(BATTLE_LOCATION_START + 67, "Mushroom Bureau - Gauntlet 3", LocationType.major_battle | LocationType.act_2, "100xp", Color.blue | Color.orange),
    "Judge Mushroom Battle": Everhood2LocationData(BATTLE_LOCATION_START + 68, "Mushroom Bureau - Finale", LocationType.major_battle | LocationType.act_2, "100xp"),
    
    # "Lucy Battle": Everhood2LocationData(BATTLE_LOCATION_START + 69, "Lucy's Room", LocationType.unique_battle | LocationType.post_dragon, "1000xp"),

    "Manifested Evil Thought 1": Everhood2LocationData(BATTLE_LOCATION_START + 70, "Irvine Pocket Dimension", LocationType.trash_battle | LocationType.act_2, "100xp", Color.blue | Color.brown | Color.orange),
    "Manifested Evil Thought 2": Everhood2LocationData(BATTLE_LOCATION_START + 71, "Irvine Pocket Dimension", LocationType.trash_battle | LocationType.act_2, "100xp", Color.blue | Color.brown | Color.orange),
    "Doopy Dragon 3D Battle": Everhood2LocationData(BATTLE_LOCATION_START + 72, "Irvine Pocket Dimension", LocationType.unique_battle | LocationType.act_2, "35xp", Color.red | Color.blue | Color.green),
    "Vanguard 3D Battle": Everhood2LocationData(BATTLE_LOCATION_START + 73, "Irvine Pocket Dimension", LocationType.major_battle | LocationType.act_2, "250xp", Color.brown | Color.green),
    
    # "Door of the Dead Battle": Everhood2LocationData(BATTLE_LOCATION_START + 74, "Lab - Pre Puzzle", LocationType.unique_battle | LocationType.pre_dragon_doors, "0xp"), # White
    "Ghost Chunky Battle": Everhood2LocationData(BATTLE_LOCATION_START + 75, "Lab - Pre Puzzle", LocationType.unique_battle | LocationType.pre_dragon_doors, "35xp", Color.purple),
    "Ghost Junkie Battle": Everhood2LocationData(BATTLE_LOCATION_START + 76, "Lab - Post Chunky", LocationType.unique_battle | LocationType.pre_dragon_doors, "35xp", Color.purple | Color.blue),
    "Ghost Franky Battle": Everhood2LocationData(BATTLE_LOCATION_START + 77, "Lab - Post Junkie", LocationType.major_battle | LocationType.pre_dragon_doors, "35xp", Color.purple | Color.green),

    # "Cazok Carrot Battle": Everhood2LocationData(BATTLE_LOCATION_START + 78, "Floor Omega", LocationType.unique_battle | LocationType.post_dragon, "50xp"),
    # "Cazok Ghost Battle": Everhood2LocationData(BATTLE_LOCATION_START + 79, "Floor Omega", LocationType.unique_battle | LocationType.post_dragon, "50xp"),
    # "Cazok Vanguard 3D Battle": Everhood2LocationData(BATTLE_LOCATION_START + 80, "Floor Omega", LocationType.unique_battle | LocationType.post_dragon, "50xp"),
    # "Cazok Battle": Everhood2LocationData(BATTLE_LOCATION_START + 81, "Floor Omega", LocationType.major_battle | LocationType.post_dragon, "950xp"),

    #Todo Categorise Better
    "Motherboard INT Battle": Everhood2LocationData(BATTLE_LOCATION_START + 82, "Smega Console - Motherboard A", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.blue | Color.red),
    "Motherboard CHAR Battle": Everhood2LocationData(BATTLE_LOCATION_START + 83, "Smega Console - Motherboard B", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.red | Color.green | Color.purple),
    "Motherboard BOOL x3 Battle": Everhood2LocationData(BATTLE_LOCATION_START + 84, "Smega Console - Motherboard B", LocationType.trash_battle | LocationType.pre_dragon_doors, "192xp"), 
    "Motherboard While Battle": Everhood2LocationData(BATTLE_LOCATION_START + 85, "Smega Console - Motherboard B", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.green | Color.yellow | Color.purple | Color.blue),
    
    "RAM N INT Battle": Everhood2LocationData(BATTLE_LOCATION_START + 86, "Smega Console - RAM", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.red | Color.blue | Color.green),
    "RAM BOOL Battle": Everhood2LocationData(BATTLE_LOCATION_START + 87, "Smega Console - RAM", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.blue | Color.orange),
    "RAM N While Battle": Everhood2LocationData(BATTLE_LOCATION_START + 88, "Smega Console - RAM", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.yellow | Color.green | Color.blue),
    "RAM SE While Battle": Everhood2LocationData(BATTLE_LOCATION_START + 89, "Smega Console - RAM", LocationType.trash_battle | LocationType.pre_dragon_doors, "128xp", Color.yellow | Color.green | Color.blue),
    "RAM SE INT Battle": Everhood2LocationData(BATTLE_LOCATION_START + 90, "Smega Console - RAM", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.red | Color.blue | Color.green),
    "RAM SE CHAR Battle": Everhood2LocationData(BATTLE_LOCATION_START + 91, "Smega Console - RAM", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.red | Color.green | Color.purple),
    "RAM SW FLOAT Battle": Everhood2LocationData(BATTLE_LOCATION_START + 92, "Smega Console - RAM", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.red | Color.blue),
    "RAM SW CHAR Battle 2": Everhood2LocationData(BATTLE_LOCATION_START + 93, "Smega Console - RAM", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.red | Color.green | Color.purple),
    "RAM SW MATRIX Battle": Everhood2LocationData(BATTLE_LOCATION_START + 94, "Smega Console - RAM", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.red | Color.blue | Color.purple),

    "Processor Gate Battle": Everhood2LocationData(BATTLE_LOCATION_START + 95, "Smega Console - Motherboard B", LocationType.major_battle | LocationType.pre_dragon_doors, "250xp", Color.green | Color.blue | Color.purple), # Also has white but not in a large quantity
    "Processor INT Battle": Everhood2LocationData(BATTLE_LOCATION_START + 96, "Smega Console - Processor A", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.blue | Color.red),
    "Processor FLOAT Battle": Everhood2LocationData(BATTLE_LOCATION_START + 97, "Smega Console - Processor B", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.blue | Color.red | Color.purple | Color.orange),
    "Processor MATRIX Battle": Everhood2LocationData(BATTLE_LOCATION_START + 98, "Smega Console - Processor B", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.red | Color.blue | Color.purple),
    "Processor BOOL Battle": Everhood2LocationData(BATTLE_LOCATION_START + 99, "Smega Console - Processor B", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.blue | Color.orange),
    "Processor CHAR Battle": Everhood2LocationData(BATTLE_LOCATION_START + 100, "Smega Console - Processor B", LocationType.trash_battle | LocationType.pre_dragon_doors, "64xp", Color.purple | Color.green | Color.red),
    "Processor WHILE Battle": Everhood2LocationData(BATTLE_LOCATION_START + 101, "Smega Console - Processor B", LocationType.trash_battle | LocationType.pre_dragon_doors, "128xp", Color.blue | Color.green | Color.orange),
    "Corrupt Irvine Battle": Everhood2LocationData(BATTLE_LOCATION_START + 102, "Smega Console - Processor B", LocationType.major_battle | LocationType.pre_dragon_doors, "1200xp", Color.red | Color.green | Color.blue | Color.orange | Color.purple),
    
    "Rock Battle Near Entrance Battle": Everhood2LocationData(BATTLE_LOCATION_START + 103, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "200xp", Color.brown | Color.purple | Color.yellow),
    "Rock Battle Near Chest Mimic Battle": Everhood2LocationData(BATTLE_LOCATION_START + 104, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "200xp", Color.brown | Color.purple | Color.yellow),
    "Mimic Chest Battle": Everhood2LocationData(BATTLE_LOCATION_START + 105, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "250xp", Color.yellow | Color.green),
    "Rock Battle In Bottom Right Battle": Everhood2LocationData(BATTLE_LOCATION_START + 138, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "200xp", Color.brown | Color.purple | Color.yellow),
    "Mimic Apple Battle": Everhood2LocationData(BATTLE_LOCATION_START + 106, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "300xp", Color.red | Color.blue),
    "Harpy Over Cliff Battle": Everhood2LocationData(BATTLE_LOCATION_START + 107, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "250xp"), # Harpy spams white notes.
    "Zombie King Bongo Battle": Everhood2LocationData(BATTLE_LOCATION_START + 108, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "300xp", Color.green | Color.brown),
    "Zombie King Zorgo Battle": Everhood2LocationData(BATTLE_LOCATION_START + 109, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "300xp", Color.green | Color.brown),
    "Zombie King Mongo Battle": Everhood2LocationData(BATTLE_LOCATION_START + 110, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "300xp", Color.green | Color.brown),
    "Rock Battle Near Zombies": Everhood2LocationData(BATTLE_LOCATION_START + 111, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "200xp", Color.brown | Color.purple | Color.yellow),
    "Harpy With Concussion Battle": Everhood2LocationData(BATTLE_LOCATION_START + 112, "Death Mountain", LocationType.trash_battle | LocationType.act_2, "250xp"), # Harpy spams white notes.
    "Crab Machine Battle": Everhood2LocationData(BATTLE_LOCATION_START + 113, "Death Mountain", LocationType.major_battle | LocationType.act_2, "1000xp", Color.red | Color.blue | Color.green),
    
    # Todo: Get Working
    # "Dmitri Battle": Everhood2LocationData(BATTLE_LOCATION_START + 114, "Tutorial Spaceship", LocationType.major_battle | LocationType.act_2, "650xp", Color.red | Color.blue | Color.purple),
    
    "Yellow Battle": Everhood2LocationData(BATTLE_LOCATION_START + 115, "Everhood 1 - Intro", LocationType.major_battle | LocationType.act_2, "800xp", Color.red | Color.green | Color.blue),
    "Cursed Castle Battle": Everhood2LocationData(BATTLE_LOCATION_START + 116, "Everhood 1 - Post Yellow", LocationType.major_battle | LocationType.act_2, "800xp", Color.purple | Color.yellow),
    "Light Being Battle": Everhood2LocationData(BATTLE_LOCATION_START + 117, "Everhood 1 - Post Castle", LocationType.unique_battle | LocationType.act_2, "600xp", Color.red | Color.green), # Blue is also there. But isn't in the final repeatable phase.
    "Slot Machine Battle": Everhood2LocationData(BATTLE_LOCATION_START + 118, "Everhood 1 - Post Castle", LocationType.unique_battle | LocationType.act_2, "500xp", Color.blue | Color.brown),
    
    "Judge Creation Battle": Everhood2LocationData(BATTLE_LOCATION_START + 119, "Deep Sea", LocationType.item | LocationType.act_3, "0xp", Color.red | Color.green | Color.blue),
    
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
