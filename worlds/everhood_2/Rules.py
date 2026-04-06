from typing import TYPE_CHECKING
from worlds.AutoWorld import World
from rule_builder.rules import Rule, CanReachRegion, CanReachLocation, Has, HasAny, HasAll, OptionFilter, True_, HasAnyCount, Filtered

from .Locations import  LocationType, all_locations, Color, Everhood2LocationData
from .Options import Colorsanity, SoulColor, DoorKeys
from .Regions import region_data_table, Connection
from .Items import colors_to_name

if TYPE_CHECKING:
    from . import Everhood2World
    
COLOR_OPTION = [OptionFilter(Colorsanity, Colorsanity.option_SingleSoulPiece, "ge")]

def get_soul_count(location_type: LocationType) -> int:
    if LocationType.act_3 in location_type:
        return 3
    if LocationType.act_2 in location_type:
        return 2
    return 1

def get_color_rule(colors: Color, location_type: LocationType) -> Rule:
    soul_count = get_soul_count(location_type)
    items = {colors_to_name[c]: soul_count for c in colors}
    rule = HasAnyCount(items, filtered_resolution=True, options=COLOR_OPTION)
    return rule

def get_entrance_name(parent_region: str, connection: Connection):
    name = connection.entrance_name
    if name is None:
        name = parent_region + " -> " + connection.connect_to
    return name

def set_everhood2_rules(world: "Everhood2World", valid_types: LocationType, red_override: bool) -> None:   
    set_connection_rules(world, valid_types)
    set_location_rules(world, red_override)


def setup_act_rules(world: "Everhood2World", valid_types: LocationType, goal: int) -> None:
    world.set_completion_rule(Has("Victory"))
    
    dragon_mirror = world.get_entrance("Dragon Mirror Room")
    world.set_rule(dragon_mirror, Has("Purple Soul Piece", options=COLOR_OPTION, filtered_resolution=True) 
                   & Has("Power Gem", world.get_needed_dragon_gem_count(valid_types)))
        
    if goal <= world.options.goal_condition.option_Dragon:
        world.create_victory_event("Time Hub")
        return

    deep_sea = world.get_entrance("Deep Sea Entrance")
    world.set_rule(deep_sea, CanReachRegion("Everhood 1 - Post Castle"))
    
    space_ship = world.get_entrance("Space Ship Entrance")    
    world.set_rule(space_ship, HasAll("Red Soul Piece", "Green Soul Piece", "Blue Soul Piece", "Yellow Soul Piece", 
                                      "Brown Soul Piece", "Purple Soul Piece", "Orange Soul Piece", options=COLOR_OPTION, filtered_resolution=True)
                               & Has("Death Coin") & HasAny("Red Soul Axe", "Green Soul Spear", "Blue Soul Knives"))
            
    if LocationType.act_3 not in valid_types:
        world.create_victory_event("Deep Sea")
        return
    
    raise NotImplementedError

def set_connection_rules(world: World, valid_types: LocationType):
    created_entrances = {e.name:e for e in world.get_entrances()}
    
    for region_name, region_data in region_data_table.items():
        if region_data.include_type not in valid_types:
            continue
            
        for connection in region_data.connecting_regions:
            entrance = created_entrances.get(get_entrance_name(region_name, connection))
            if entrance is None:
                continue                
                               
            rule = True_()
            if connection.key is not None:
                if connection.always_include_key:
                    rule = rule & Has(connection.key, connection.key_count)
                else:
                    rule = rule & Has(connection.key, connection.key_count, filtered_resolution=True, options=[OptionFilter(DoorKeys, 1)])
                
            if connection.death_coin > 0:
                rule = rule & Has("Death Coin", connection.death_coin)
                
            if connection.color != 0:
                rule = rule & get_color_rule(connection.color, region_data.include_type)
                
            if connection.location is not None:
                if connection.skip_location_in_doorkeys:
                    rule = rule & CanReachLocation(connection.location, filtered_resolution=True, options=[OptionFilter(DoorKeys, 0)])
                else:
                    rule = rule & CanReachLocation(connection.location)
            
            if connection.custom_rule is not None:
                rule = rule & connection.custom_rule

            world.set_rule(entrance, rule)


def set_location_rules(world: World, red_override:bool):
    for location in world.get_locations():        
        location_data = all_locations.get(location.name)
        if location_data is None:
            continue
        
        if location_data.skip_on_red_soul and red_override:
            continue

        rule = True_()
        if location_data.color != 0:
            rule = rule & get_color_rule(location_data.color, location_data.type)
            
        if location_data.locations is not None:
            for loc in location_data.locations:
                rule = rule & CanReachLocation(loc)
                
        if location_data.custom_color_rule is not None:
            rule = rule & Filtered(location_data.custom_color_rule, options=COLOR_OPTION, filtered_resolution=True)
        
        world.set_rule(location, rule)