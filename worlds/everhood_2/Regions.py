from typing import Dict, List, NamedTuple
from .Locations import LocationType, Color

class Connection(NamedTuple):
    connect_to: str
    location: str = None
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
        Connection("Marzian Era 1000", "Dimension Master Battle", "Progressive Marzian Key", 2),
        Connection("Marzian Era 2000", "Dimension Portal Battle", "Progressive Marzian Key", 3),
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
    "Eternal War - Tomato Rampages": Everhood2RegionData([Connection("Eternal War - Bridge And Dungeon", "Melon Battle")]), #Todo: Color Requirements
    "Eternal War - Bridge And Dungeon": Everhood2RegionData([Connection("Eternal War - Tournament A", "Capsicum Battle")]), #Todo: Color Requirements
    "Eternal War - Tournament A": Everhood2RegionData([Connection("Eternal War - Tournament B", "Carrot Mage Battle")]), #Todo: Color Requirements
    "Eternal War - Tournament B": Everhood2RegionData([Connection("Eternal War - Post Win", "Juice Master#4671 Battle")]), #Todo: Color Requirements
    "Eternal War - Post Win": Everhood2RegionData([]),
        
    "Marzian Era 0 - Mines A": Everhood2RegionData([Connection("Marzian Era 0 - Mines B", "Hyena Battle Screech")]),
    "Marzian Era 0 - Mines B": Everhood2RegionData([Connection("Marzian Era 0 - Mines C", "Howler & Razor Battle")]),
    "Marzian Era 0 - Mines C": Everhood2RegionData([Connection("Marzian Era 0 - Base A", "Feugo Battle")]),
    "Marzian Era 0 - Base A": Everhood2RegionData([Connection("Marzian Era 0 - Base B", "Insect Abomination Battle")]),
    "Marzian Era 0 - Base B": Everhood2RegionData([Connection("Marzian Era 0 - Base C", "Anxious Chase Battle")]),
    "Marzian Era 0 - Base C": Everhood2RegionData([Connection("Marzian Era 0 - Prison")]), #Todo: Custom Rule
    "Marzian Era 0 - Base D": Everhood2RegionData([]), #Todo: Custom Rule
    
    "Marzian Era 1000": Everhood2RegionData(["Infinity Hub"]),
    "Marzian Era 2000": Everhood2RegionData(["Infinity Hub"]),
    "Marzian Era 3000": Everhood2RegionData(["Infinity Hub"], LocationType.post_dragon),
    "Marzian Era 4000": Everhood2RegionData(["Infinity Hub"], LocationType.post_dragon),
    "Marzian Era 5000": Everhood2RegionData(["Infinity Hub"], LocationType.post_dragon),
    
    # Todo: Region Removal of irrelevant regions
    "Smega Console - Motherboard A": Everhood2RegionData([Connection("Smega Console - Motherboard B", "Motherboard INT Battle")], LocationType.pre_dragon_doors),
    "Smega Console - Motherboard B": Everhood2RegionData(
        [
            Connection("Smega Console - RAM"), 
            Connection("Smega Console - Processor", "Processor Gate Battle"),
            Connection("Smega Console - Doctor Dump", "Corrupt Irvine Battle")
        ], 
        LocationType.pre_dragon_doors
    ), 
    "Smega Console - RAM": Everhood2RegionData([]),
    "Smega Console - Processor A": Everhood2RegionData([Connection("Smega Console - Processor B", "Processor INT Battle")]),
    "Smega Console - Processor B": Everhood2RegionData([Connection("Smega Console - Irvine")]), #Todo: Custom Rule. Blue | Green | Red && Blue | Orange
    "Smega Console - Irvine": Everhood2RegionData([]),
    "Smega Console - Doctor Dump": Everhood2RegionData([]),
    
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
