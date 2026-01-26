from typing import TYPE_CHECKING
from worlds.AutoWorld import World, CollectionState
from BaseClasses import Location, Entrance

from .Locations import LocationType, all_locations, Color, Everhood2LocationData
from .Options import CompletionCondition
from .Regions import region_data_table, Connection
from .Items import colors_to_name

if TYPE_CHECKING:
    from . import Everhood2World

def set_everhood2_rules(world: "Everhood2World", valid_types: LocationType, door_keys: bool, colorsanity: bool, red_override: bool, goal: int) -> None:        
    if world.options.door_keys.value:
        set_door_key_rules(world, valid_types, colorsanity)

    if LocationType.hillbert in valid_types:
        set_hillbert_rules(world, valid_types)
        
    if colorsanity:
        set_colorsanity_location_rules(world, valid_types, red_override)

    set_additional_region_rules(world, valid_types, door_keys, colorsanity, red_override)


def setup_act_rules(world: "Everhood2World", valid_types: LocationType, colorsanity: bool, goal: int) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
    
    if colorsanity:
        world.get_entrance("Dragon Mirror Room").access_rule = lambda state: state.has("Purple", world.player) and \
                                                                             state.has("Power Gem", world.player, world.get_needed_dragon_gem_count(valid_types))
    else:
        world.get_entrance("Dragon Mirror Room").access_rule = lambda state: state.has("Power Gem", world.player, world.get_needed_dragon_gem_count(valid_types))
    
    if goal <= world.options.goal_condition.option_Dragon:
        world.create_victory_event("Time Hub")
        return

    deep_sea = world.get_entrance("Deep Sea Entrance")
    world.multiworld.register_indirect_condition(world.get_region("Everhood 1 - Post Castle"), deep_sea)
    if colorsanity:
        deep_sea.access_rule = lambda state: (state.has_all(["Red", "Blue", "Green", "Yellow", "Brown", "Purple", "Orange"], world.player) 
                                                                             and state.can_reach_region("Everhood 1 - Post Castle", world.player))
    else:
        deep_sea.access_rule = lambda state: state.can_reach_region("Everhood 1 - Post Castle", world.player)  
    
    if LocationType.act_3 not in valid_types:
        world.create_victory_event("Deep Sea")
        return
    
    raise NotImplementedError
        
def set_door_key_rules(world: World, valid_types: LocationType, colorsanity: bool) -> None:
    for key, data in region_data_table.items():
        if data.include_type not in valid_types:
            continue
        
        for connection in data.connecting_regions:
            otherData = region_data_table[connection.connect_to]
            if otherData.include_type not in valid_types:
                continue
            
            if connection.key is None:
                continue

            if connection.color != 0:
                raise Exception("Location Has More Rules than intended. MOVE TO TESTS")
            
            if connection.location is not None:          
                location = all_locations[connection.location]
                if location.region == key and location.type in valid_types:
                    entrance = world.get_entrance(get_entrance_name(key, connection))
                    entrance.access_rule = lambda state, c=connection: \
                        state.has(c.key, world.player, c.key_count) and state.can_reach_location(c.location, world.player)
                    world.multiworld.register_indirect_condition(world.get_region(location.region), entrance)                    
                else:
                    create_key_reach_rule(world, key, connection, location, colorsanity)
            else:            
                world.get_entrance(get_entrance_name(key, connection)).access_rule = lambda state, c=connection: state.has(c.key, world.player, c.key_count)


def set_hillbert_rules(world: World, valid_types: LocationType) -> None:
    #Todo: Need to double check if these need indirect connections
    
    # world.get_location("Floor 23 Key").access_rule = lambda state: state.has_any(["Neon Forest Key", "Eternal War Key", "Progressive Marzian Key"], world.player)

    hillbert_rule(world, world.get_location("Gold Key"), valid_types, "Juice Master#4671 Battle", "Dimension Master Battle")
        
    if LocationType.pre_dragon_doors not in valid_types:
        return

    hillbert_rule(world, world.get_location("Green Key"), valid_types, "Dimension Portal Battle")
    hillbert_rule(world, world.get_location("Pinecone Key"), valid_types, "Blue Stonegrunt Battle")


def hillbert_rule(world: World, location: Location, valid_types: LocationType, locA: str, locB: str | None = None):
    battleA = all_locations[locA]
    if battleA.type not in valid_types:
        world.get_region(battleA.region).add_event(locA)
        
    if locB is not None:
        battleB = all_locations[locB]
        if battleB.type not in valid_types:
            world.get_region(battleB.region).add_event(locB)

        location.access_rule = lambda state: state.can_reach_location(locA, world.player) and state.can_reach_location(locB, world.player)
    else:
        location.access_rule = lambda state: state.can_reach_location(locA, world.player)


def set_colorsanity_location_rules(world: World, valid_types: LocationType, red_override: bool) -> None:
    # Todo: Doesn't handle region logic.
    for key, data in all_locations.items():
        # Certain fights feature plenty of white notes which will always be available.
        # Todo: Also lock white?
        if data.color == 0 or data.type not in valid_types:
            continue

        if red_override and (key == "Capsicum Battle" or key == "Juice Master#4671 Battle"):
            colors = get_colors(Color.red)
            world.get_location(key).access_rule = lambda state, c=colors: state.has_any(c, world.player)
        else:
            colors = get_colors(data.color)
            world.get_location(key).access_rule = lambda state, c=colors: state.has_any(c, world.player)

    # Custom Rules
    set_complex_color(world, "Smega Console - Chest Behind Motherboard Bool",
                      [Color.red | Color.green | Color.purple, Color.blue | Color.red, Color.orange | Color.blue], valid_types)
    set_complex_color(world, "Motherboard BOOL x3 Battle",
                      [Color.red | Color.green | Color.purple, Color.blue | Color.red, Color.orange | Color.blue], valid_types)
    set_complex_color(world, "Howler & Razor Battle", [Color.green | Color.blue, Color.green | Color.orange], valid_types)
    set_complex_color(world, "Howler & Razor & Maggot Battle", [Color.green | Color.blue, Color.green | Color.orange], valid_types)
    set_complex_color(world, "Opus & Screech Battle", [Color.green | Color.blue, Color.green | Color.orange], valid_types)

def set_additional_region_rules(world: World, valid_types: LocationType, door_keys: bool, colorsanity: bool, red_override: bool) -> None:
    # Todo: Doesn't handle region logic.
    for key, data in region_data_table.items():
        if data.include_type not in valid_types:
            continue
            
        # Certain fights feature plenty of white notes which will always be available.
        # Todo: Also lock white?
        for connection in data.connecting_regions:
            if connection.key is not None and door_keys:
                continue
                
            if connection.custom_rule is not None:
                world.get_entrance(get_entrance_name(key, connection)).access_rule = lambda state, c=connection: c.custom_rule(state, world)
                continue

            if connection.death_coin > 0:
                world.get_entrance(get_entrance_name(key, connection)).access_rule = lambda state, c=connection: state.has("Death Coin", world.player, c.death_coin)
                continue

            name = get_entrance_name(key, connection)                    
            if connection.location:
                create_indirect(world, world.get_entrance(name), key, connection, valid_types, colorsanity)                
            elif connection.color != 0 and colorsanity:
                if red_override and (connection.key == "Capsicum Battle" or connection.key == "Juice Master#4671 Battle"):
                    colors = get_colors(Color.red)
                    world.get_entrance(name).access_rule = lambda state, c=colors: state.has_any(c, world.player)
                else:
                    colors = get_colors(connection.color)
                    world.get_entrance(name).access_rule = lambda state, c=colors: state.has_any(c, world.player)


def set_complex_color(world: World, location: str, colors: list[Color], valid_types: LocationType) -> None:
    data = all_locations.get(location)    
    if data.type not in valid_types:
        return 
    
    all_colors = []
    for color in colors:
        all_colors.append(get_colors(color))
    
    world.get_location(location).access_rule = lambda state, a=all_colors: get_complex_color(state, a, world.player)
    

def get_complex_color(state: CollectionState, all_colors: list[list[str]], player: int):
    for colors in all_colors:
        if not state.has_any(colors, player):
            return False
    return True


def get_colors(color : Color) -> list[str]:
    colors = []
    for col in color:
        colors.append(colors_to_name[col])
    return colors


def get_entrance_name(parent_region: str, connection: Connection):
    name = connection.entrance_name
    if name is None:
        name = parent_region + " -> " + connection.connect_to
    return name


def create_key_reach_rule(world: World, parent_region: str, connection: Connection, battle: Everhood2LocationData, colorsanity: bool):
    name = get_entrance_name(parent_region, connection)
    entrance = world.get_entrance(name)
    world.multiworld.register_indirect_condition(world.get_region(battle.region), entrance)

    if colorsanity and battle.color != 0:
        colors = get_colors(battle.color)
        entrance.access_rule = lambda state: state.has_any(colors, world.player) \
                                   and state.has(connection.key, world.player, connection.key_count) \
                                   and state.can_reach_region(battle.region, world.player)
    else:
        entrance.access_rule = lambda state: state.has(connection.key, world.player, connection.key_count) \
                                             and state.can_reach_region(battle.region, world.player)
        
def create_indirect(world: World, entrance: Entrance, parent_region: str, connection: Connection, valid_types: LocationType, colorsanity: bool):
    battle = all_locations[connection.location]
    if battle.region == parent_region:
        if battle.type in valid_types:
            entrance.access_rule = world.get_location(connection.location).access_rule
        elif colorsanity and battle.color != 0:
            colors = get_colors(battle.color)
            entrance.access_rule = lambda state: state.has_any(colors, world.player)
    elif battle.type in valid_types:
        entrance.access_rule = lambda state: state.can_reach_location(connection.location, world.player)
        world.multiworld.register_indirect_condition(world.get_region(battle.region), entrance)
    elif colorsanity and battle.color != 0:
        world.get_region(battle.region).add_event(connection.location)        
        entrance.access_rule = lambda state: state.can_reach_location(connection.location, world.player)
        world.multiworld.register_indirect_condition(world.get_region(battle.region), entrance)

def create_indirect_key(world: World, entrance: Entrance, parent_region: str, connection: Connection, valid_types: LocationType):
    battle = all_locations[connection.location]
    if battle.region == parent_region:
        raise Exception("This shouldn't happen.")
    elif battle.type in valid_types:
        entrance.access_rule = lambda state: state.can_reach_location(connection.location, world.player) and state.has(connection.key, world.player, connection.key_count)
        world.multiworld.register_indirect_condition(world.get_region(battle.region), entrance)
    else:
        world.get_region(battle.region).add_event(connection.location)
        entrance.access_rule = lambda state: state.can_reach_location(connection.location, world.player) and state.has(connection.key, world.player, connection.key_count)
        world.multiworld.register_indirect_condition(world.get_region(battle.region), entrance)