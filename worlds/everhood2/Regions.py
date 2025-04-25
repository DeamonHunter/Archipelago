from typing import Dict, List, NamedTuple


class Everhood2RegionData(NamedTuple):
    connecting_regions: List[str] = []

# Todo: Get proper names for various areas
region_data_table: Dict[str, Everhood2RegionData] = {
    "Menu": Everhood2RegionData(["Tutorial Hub"]),
    "Tutorial Hub": Everhood2RegionData(), # To Be Connected to a soul color
    "Infinity Hub": Everhood2RegionData(["Eternal War - Desert", "Neon City"]),
    "Eternal War - Desert": Everhood2RegionData(["Eternal War - Castle"]),
    "Eternal War - Castle": Everhood2RegionData(["Infinity Hub"]),
    "Neon City": Everhood2RegionData(["Neon Jungle", "Hillbert Hotel"]),
    "Neon Jungle": Everhood2RegionData(["Neon City"]),
    "Hillbert Hotel": Everhood2RegionData(["Infinity Hub", "Hangout Hub", "End Hub", "Floor 23", "Floor Gold", "Floor Green", 
                                           "Floor Pinecone", "Battle Colosseum", "Dunkey Room", "Sam's House", "Lucy's House", 
                                           "Mushroom Dance Room"]), # Also "Toilet A Room", "Toilet B Room"
    # Todo: For ER type stuff, will need to add rooms here
    "Marzian Era 0 - Mining Area": Everhood2RegionData(["Marzian Era 0 - Mining Base"]),
    "Marzian Era 0 - Mining Base": Everhood2RegionData(["Infinity Hub"]),
    "Marzian Era 1000": Everhood2RegionData(["Infinity Hub"]),
    "Marzian Era 2000": Everhood2RegionData(["Infinity Hub"]),
    "Marzian Era 3000": Everhood2RegionData(["Infinity Hub"]),
    "Marzian Era 4000": Everhood2RegionData(["Infinity Hub"]),
    "Marzian Era 5000": Everhood2RegionData(["Infinity Hub"]),
    
    # Hillbert Hotel Rooms Todo: Maybe make an option to exclude these areas
    "Floor 23": Everhood2RegionData(["Hillbert Hotel"]),
    "Floor Gold": Everhood2RegionData(["Hillbert Hotel"]),
    "Floor Green": Everhood2RegionData(["Hillbert Hotel"]),
    "Floor Pinecone": Everhood2RegionData(["Hillbert Hotel"]),
    "Battle Collosseum": Everhood2RegionData(["Hillbert Hotel", "End Hub"]),
    "Dunkey Room": Everhood2RegionData(["Hillbert Hotel"]), #Todo: Does this have anything?
    "Sam's House": Everhood2RegionData(["Hillbert Hotel"]),
    "Lucy's House": Everhood2RegionData(["Hillbert Hotel"]),
}
