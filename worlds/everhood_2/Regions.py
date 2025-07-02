from typing import Dict, List, NamedTuple
from .Locations import LocationType, Color

class Connection(NamedTuple):
    connect_to: str
    color: Color = 0
    key: str = None
    key_count: int = 1
    
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
        Connection("Eternal War - Battlefield", key="Eternal War Key"),
        Connection("Neon City - City", key="Neon Forest Key"),
        Connection("Marzian Era 0 - Mining Area", key="Progressive Marzian Key"),
        Connection("Marzian Era 1000", key="Progressive Marzian Key", key_count=2),
        Connection("Marzian Era 2000", key="Progressive Marzian Key", key_count=3),
        Connection("Smega Console", key="Smega Console Key"),
        Connection("Home Town", key="Home Town Key"),
        Connection("Lab", key="Lab Key"),
    ]),

    # Neon City Regions.
    "Neon City - City": Everhood2RegionData([
        Connection("Neon City - Jungle", Color.green | Color.blue | Color.purple), 
        Connection("Hillbert Hotel", Color.green | Color.blue)]
    ),
    "Neon City - Jungle": Everhood2RegionData([Connection("Neon City - Void", Color.green | Color.purple)]),
    "Neon City - Abyss": Everhood2RegionData([]), # "Neon City - City" Removed because unnecessary without ER
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
    "Eternal War - Tomato Rampages": Everhood2RegionData(["Eternal War - Bridge"], Color.red), #Todo: Color Requirements
    "Eternal War - Bridge": Everhood2RegionData(["Eternal War - Dungeon"], Color.red), #Todo: Color Requirements
    "Eternal War - Dungeon": Everhood2RegionData(["Eternal War - Tournament 1"], Color.red), #Todo: Color Requirements
    "Eternal War - Tournament 1": Everhood2RegionData(["Eternal War - Tournament 2"], Color.red), #Todo: Color Requirements
    "Eternal War - Tournament 2": Everhood2RegionData([]),
        
        
    "Marzian Era 0 - Mining Area": Everhood2RegionData(["Marzian Era 0 - Mining Base"]),
    "Marzian Era 0 - Mining Base": Everhood2RegionData(["Infinity Hub"]),
    "Marzian Era 1000": Everhood2RegionData(["Infinity Hub"]),
    "Marzian Era 2000": Everhood2RegionData(["Infinity Hub"]),
    "Marzian Era 3000": Everhood2RegionData(["Infinity Hub"], LocationType.post_dragon),
    "Marzian Era 4000": Everhood2RegionData(["Infinity Hub"], LocationType.post_dragon),
    "Marzian Era 5000": Everhood2RegionData(["Infinity Hub"], LocationType.post_dragon),
    
    # Todo: Region Removal of irrelevant regions
    "Smega Console": Everhood2RegionData(["Infinity Hub"], LocationType.pre_dragon_doors), # Todo: May need splitting up?
    "Home Town": Everhood2RegionData(["Infinity Hub"], LocationType.pre_dragon_doors),
    "Lab": Everhood2RegionData(["Infinity Hub"], LocationType.pre_dragon_doors),
    
    # Hillbert Hotel Rooms Todo: Maybe make an option to exclude these areas
    "Floor 23": Everhood2RegionData(["Hillbert Hotel"], LocationType.hillbert),
    "Floor Gold": Everhood2RegionData(["Hillbert Hotel"], LocationType.hillbert),
    "Floor Green": Everhood2RegionData(["Hillbert Hotel"], LocationType.hillbert),
    "Floor Pinecone": Everhood2RegionData(["Hillbert Hotel"], LocationType.hillbert),
    "Battle Collosseum": Everhood2RegionData(["Hillbert Hotel", "End Hub"], LocationType.colosseum),
    "Dunkey Room": Everhood2RegionData(["Hillbert Hotel"], LocationType.hillbert | LocationType.post_dragon), #Todo: Does this have anything?
    "Sam's House": Everhood2RegionData(["Hillbert Hotel"], LocationType.post_dragon),
    "Lucy's House": Everhood2RegionData(["Hillbert Hotel"], LocationType.hillbert | LocationType.post_dragon),
}
