from typing import TYPE_CHECKING
from worlds.AutoWorld import World
from .Locations import LocationType

if TYPE_CHECKING:
    from . import Everhood2World

def set_everhood2_rules(world: "Everhood2World", valid_types: LocationType):
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Power Gem", world.player, 3)
    
    if world.options.door_keys.value:
        set_door_key_rules(world, valid_types)

    if LocationType.hillbert in valid_types:
        set_door_key_rules(world, valid_types)


def set_door_key_rules(world: World, valid_types: LocationType) -> None:
    world.get_entrance("Infinity Hub -> Neon City").access_rule = lambda state: state.has("Neon Forest Key", world.player)
    world.get_entrance("Infinity Hub -> Marzian Era 0 - Mining Area").access_rule = lambda state: state.has("Progressive Marzian Key", world.player)
    world.get_entrance("Infinity Hub -> Marzian Era 1000").access_rule = lambda state: state.has("Progressive Marzian Key", world.player, 2)
    world.get_entrance("Infinity Hub -> Marzian Era 2000").access_rule = lambda state: state.has("Progressive Marzian Key", world.player, 3)
    world.get_entrance("Infinity Hub -> Eternal War - Battlefield").access_rule = lambda state: state.has("Eternal War Key", world.player)
    world.get_entrance("Infinity Hub -> Smega Console").access_rule = lambda state: state.has("Smega Console Key", world.player)
    world.get_entrance("Infinity Hub -> Home Town").access_rule = lambda state: state.has("Smega Console Key", world.player)
    world.get_entrance("Infinity Hub -> Lab").access_rule = lambda state: state.has("Lab Key", world.player)
    
    
    # world.get_entrance("Infinity Hub -> Marzian Era 3000").access_rule = lambda state: state.has("Progressive Marzian Key", world.player, 4)
    # world.get_entrance("Infinity Hub -> Marzian Era 4000").access_rule = lambda state: state.has("Progressive Marzian Key", world.player, 5)
    
def set_hillbert_rules(world: World, valid_types: LocationType, door_keys: bool) -> None: 
    world.get_entrance("Hillbert Hotel -> Floor 23").access_rule = lambda state: state.has("Floor 23 Key", world.player)
    world.get_location("Floor 23 Complete Chest").access_rule = lambda state: state.has("Floor 23 Key", world.player)

    world.get_entrance("Hillbert Hotel -> Floor Gold").access_rule = lambda state: state.has("Gold Key", world.player)
    world.get_location("Floor Gold Complete Chest").access_rule = lambda state: state.has("Gold Key", world.player)

    if LocationType.cosmetic in valid_types:
        world.get_location("Cat Ears").access_rule = lambda state: state.has("Floor 23 Key", world.player)
        world.get_location("Cat Ears Bald").access_rule = lambda state: state.has("Floor 23 Key", world.player)
        world.get_location("Oingo Boingo").access_rule = lambda state: state.has("Gold Key", world.player)

    if not door_keys:
        return 

    # Todo: We could probably get rid of the first 2 rules as they are technically always true unless we have entrance rando 
    #  #Todo: Is this the right requirements? Do the Home Town, Lab and Smega Areas count? (I don't think so as that is sequence breaking.)
    world.get_location("Floor 23 Key").access_rule = lambda state: state.has_any(["Neon Forest Key", "Eternal War Key", "Progressive Marzian Key"], world.player)
    world.get_location("Floor Gold Key").access_rule = lambda state: state.has_any(["Neon Forest Key", "Eternal War Key", "Progressive Marzian Key"], world.player)
    world.get_location("Floor Green Key").access_rule = lambda state: state.has_from_list_unique(["Neon Forest Key", "Eternal War Key", "Progressive Marzian Key"], world.player, 2)
    world.get_location("Floor Green Key").access_rule = lambda state: state.has_all(["Neon Forest Key", "Eternal War Key", "Progressive Marzian Key"], world.player)
    