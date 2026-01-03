from typing import Dict, List, NamedTuple, Callable

from BaseClasses import CollectionState
from .Locations import LocationType, Color

class Connection(NamedTuple):
    connect_to: str
    location: str = None
    key: str = None
    key_count: int = 1
    color: Color = 0
    entrance_name: str = None
    custom_rule: Callable[[CollectionState], bool] = None
    
class Everhood2RegionData(NamedTuple):
    connecting_regions: List[Connection]
    include_type: LocationType = LocationType.item

# Todo: Properly name areas
# These regions roughly replicate real regions, though are split via fights.
region_data_table: Dict[str, Everhood2RegionData] = {
    "Menu": Everhood2RegionData([Connection("Tutorial Hub")]),
    # Physically this is connected through a route, but you can always get through your starting route.
    "Tutorial Hub": Everhood2RegionData([Connection("Infinity Hub")]),     
    
    #Starting Hub.
    "Infinity Hub": Everhood2RegionData([
        Connection("Eternal War - Tomato Rampages", key="Eternal War Key"),
        Connection("Neon City - Pre Homonculus", key="Neon Forest Key"),
        Connection("Marzian Era 0 - Mines A", key="Progressive Marzian Key"),
        Connection("Marzian Era 1000", "Dimension Master Battle", "Progressive Marzian Key", 2),
        Connection("Marzian Era 2000", "Dimension Portal Battle", "Progressive Marzian Key", 3),
        Connection("Smega Console - Motherboard A", key="Smega Console Key"),
        Connection("Home Town", key="Home Town Key"),
        Connection("Lab - Pre Puzzle", key="Lab Key"),
        Connection("Time Hub")
    ]),

    # Neon City Regions.
    "Neon City - Pre Homonculus": Everhood2RegionData([
        Connection("Neon City - Post Homonculus", "Homonculus Battle"), 
        Connection("Hillbert Hotel",  "Cowgirl Homonculus Battle")] # Requires a fight that has no color reqs and no reward.
    ),
    "Neon City - Post Homonculus": Everhood2RegionData([Connection("Neon City - Post Cowgirl Homonculus", "Cowgirl Homonculus Battle")]),
    "Neon City - Post Cowgirl Homonculus": Everhood2RegionData([]),
    "Hillbert Hotel": Everhood2RegionData(
        [
            # Removed because unnecessary without ER
            # "Infinity Hub", "Hangout Hub", "End Hub", 
            Connection("Floor 23", key="Floor 23 Key"),
            Connection("Floor Gold", key="Gold Key"),
            Connection("Floor Green", key="Green Key"),
            Connection("Floor Pinecone", key="Pinecone Key"),
            # Not Implemented Yet
            # "Battle Colosseum", "Dunkey Room", "Sam's House", "Lucy's House", "Mushroom Dance Room" Temporarily Disabled
            # Also "Toilet A Room", "Toilet B Room". Useless rooms but can be for ER
        ]
    ), 
    
    # Eternal War
    "Eternal War - Tomato Rampages": Everhood2RegionData([Connection("Eternal War - Bridge And Dungeon", "Melon Battle")]), 
    "Eternal War - Bridge And Dungeon": Everhood2RegionData([Connection("Eternal War - Tournament A", "Capsicum Battle")]),
    "Eternal War - Tournament A": Everhood2RegionData([Connection("Eternal War - Tournament B", "Carrot Mage Battle")]),
    "Eternal War - Tournament B": Everhood2RegionData([Connection("Eternal War - Post Win", "Juice Master#4671 Battle")]),
    "Eternal War - Post Win": Everhood2RegionData([]),
        
    "Marzian Era 0 - Mines A": Everhood2RegionData([Connection("Marzian Era 0 - Mines B", "Hyena Battle Screech")]),
    "Marzian Era 0 - Mines B": Everhood2RegionData([Connection("Marzian Era 0 - Mines C", "Howler & Razor Battle")]),
    "Marzian Era 0 - Mines C": Everhood2RegionData([Connection("Marzian Era 0 - Base A", "Feugo Battle")]),
    "Marzian Era 0 - Base A": Everhood2RegionData([Connection("Marzian Era 0 - Base B", "Insect Abomination Battle")]),
    "Marzian Era 0 - Base B": Everhood2RegionData([Connection("Marzian Era 0 - Base C", "Anxious Chase Battle")]),
    "Marzian Era 0 - Base C": Everhood2RegionData(
        [
            Connection("Marzian Era 0 - Base D", "Howler & Razor & Maggot Battle"), 
            Connection("Marzian Era 0 - Base D", "Opus & Screech Battle", entrance_name="Marzian Era 0 - Base C -> Marzian Era 0 - Base D Alt")
        ]
    ),
    "Marzian Era 0 - Base D": Everhood2RegionData([]),
    
    "Marzian Era 1000": Everhood2RegionData([]),
    "Marzian Era 2000": Everhood2RegionData([]),
    "Marzian Era 3000": Everhood2RegionData([], LocationType.post_dragon),
    "Marzian Era 4000": Everhood2RegionData([], LocationType.post_dragon),
    "Marzian Era 5000": Everhood2RegionData([], LocationType.post_dragon),
    
    # Todo: Region Removal of irrelevant regions
    "Smega Console - Motherboard A": Everhood2RegionData([Connection("Smega Console - Motherboard B", "Motherboard INT Battle")], LocationType.pre_dragon_doors),
    "Smega Console - Motherboard B": Everhood2RegionData(
        [
            Connection("Smega Console - RAM"), 
            Connection("Smega Console - Processor A", "Processor Gate Battle"),
            Connection("Smega Console - Doctor Dump", "Corrupt Irvine Battle")
        ], 
        LocationType.pre_dragon_doors
    ), 
    "Smega Console - RAM": Everhood2RegionData([]),
    "Smega Console - Processor A": Everhood2RegionData([Connection("Smega Console - Processor B", "Processor INT Battle")]),
    "Smega Console - Processor B": Everhood2RegionData([Connection("Smega Console - Irvine")]), #Todo: Custom Rule. Blue | Green | Red && Blue | Orange
    "Smega Console - Irvine": Everhood2RegionData([]),
    "Smega Console - Doctor Dump": Everhood2RegionData([]),
    
    "Home Town": Everhood2RegionData([], LocationType.pre_dragon_doors),
    "Lab - Pre Puzzle": Everhood2RegionData([Connection("Lab - Post Chunky", "Ghost Chunky Battle")], LocationType.pre_dragon_doors),
    "Lab - Post Chunky": Everhood2RegionData([Connection("Lab - Post Junkie", "Ghost Junkie Battle")], LocationType.pre_dragon_doors),
    "Lab - Post Junkie": Everhood2RegionData([], LocationType.pre_dragon_doors),
    
    # Hillbert Hotel Rooms Todo: Maybe make an option to exclude these areas
    "Floor 23": Everhood2RegionData([Connection("Floor 23 - Smega", color=(Color.green | Color.blue)), Connection("Floor 23 - Rewards", "Rasputin Battle")], LocationType.hillbert),
    "Floor 23 - Smega": Everhood2RegionData([], LocationType.hillbert),
    "Floor 23 - Rewards": Everhood2RegionData([], LocationType.hillbert),
    
    "Floor Gold": Everhood2RegionData([Connection("Floor Gold - Post Bobo", "Bobo (Drunk) Battle")], LocationType.hillbert),
    "Floor Gold - Post Bobo": Everhood2RegionData([], LocationType.hillbert),
    
    "Floor Green": Everhood2RegionData([], LocationType.hillbert),
    
    "Floor Pinecone": Everhood2RegionData([Connection("Floor Pinecone - Post Squirrels", "Squirrels Battle")], LocationType.hillbert),
    "Floor Pinecone - Post Squirrels": Everhood2RegionData([], LocationType.hillbert),
    
    # "Battle Collosseum": Everhood2RegionData(["Hillbert Hotel", "End Hub"], LocationType.colosseum),
    # "Dunkey Room": Everhood2RegionData(["Hillbert Hotel"], LocationType.hillbert | LocationType.post_dragon), #Todo: Does this have anything?
    # "Sam's House": Everhood2RegionData(["Hillbert Hotel"], LocationType.post_dragon),
    # "Lucy's House": Everhood2RegionData(["Hillbert Hotel"], LocationType.hillbert | LocationType.post_dragon),
    
    "Time Hub": Everhood2RegionData(
        [
            Connection("Mushroom Bureau - Entrance", key="Mushroom Door Key"),
            Connection("Mushroom Dance Room", key="Smelly Key"),
            Connection("Irvine Pocket Dimension", key="3 Dimensional Key"),
        ],
        LocationType.act_2
    ),

    "Mushroom Bureau - Entrance": Everhood2RegionData(
        [
            Connection("Mushroom Bureau - Sun"),
            Connection("Mushroom Bureau - Moon"),
            Connection("Mushroom Bureau - Finale", custom_rule= lambda state: state.has_any(["Moon Emblem", "Sun Emblem"])),
        ],
        LocationType.act_2
    ),
    "Mushroom Bureau - Sun": Everhood2RegionData([], LocationType.act_2),
    "Mushroom Bureau - Moon": Everhood2RegionData([Connection("Mushroom Bureau - Gauntlet 1")], LocationType.act_2),
    "Mushroom Bureau - Gauntlet 1": Everhood2RegionData([Connection("Mushroom Bureau - Gauntlet 2", color = Color.blue | Color.yellow)], LocationType.act_2),
    "Mushroom Bureau - Gauntlet 2": Everhood2RegionData([Connection("Mushroom Bureau - Gauntlet 3", color = Color.yellow | Color.blue | Color.brown)], LocationType.act_2),
    "Mushroom Bureau - Gauntlet 3": Everhood2RegionData([], LocationType.act_2, ),
    "Mushroom Bureau - Finale": Everhood2RegionData([], LocationType.act_2 | LocationType.post_dragon),
    
}
