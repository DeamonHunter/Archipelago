from math import floor

from worlds.AutoWorld import World, WebWorld
from BaseClasses import Region, Item, Tutorial, ItemClassification
from typing import ClassVar, Type
from Options import PerGameCommonOptions, OptionError

from .Options import Everhood2Options, everhood2_option_groups
from .Items import Everhood2Item, all_items, item_groups, misc_items, door_randomizer_keys, colors, name_to_color
from .Locations import Everhood2Location, all_locations, LocationType, Color
from .Regions import region_data_table
from .Rules import set_everhood2_rules, setup_act_rules
# from .Presets import Everhood2Presets


class Everhood2WebWorld(WebWorld):
    theme = "partyTime"

    bug_report_page = "https://github.com/DeamonHunter/ArchipelagoEverhood2/issues"
    setup_en = Tutorial(
        "Mod Setup and Use Guide",
        "A guide to setting up the Everhood 2 Archipelago Mod on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["DeamonHunter"]
    )
    tutorials = [setup_en]
    # options_presets = Everhood2Presets
    option_groups = everhood2_option_groups


class Everhood2World(World):
    """Everhood 2 is a psychedelic rpg cross a rhythm game. Dodge notes sent by enemies and reflect those notes back to them."""

    # World Options
    game = "Everhood 2"
    options_dataclass: ClassVar[Type[PerGameCommonOptions]] = Everhood2Options
    options: Everhood2Options

    topology_present = False
    web = Everhood2WebWorld()

    # Necessary Data
    
    item_name_to_id = {name: code.code for name, code in all_items.items()}
    location_name_to_id = {name: code.code for name, code in all_locations.items()}
    item_name_groups = item_groups
    
    def generate_early(self) -> None:
        if self.options.goal_condition.value >= self.options.goal_condition.option_Riley:
            raise OptionError("Act 3 and beyond are not implemented yet. Please choose either Dragon or Judge Creation.")
    
    def create_item(self, name: str) -> Item:
        item = all_items[name]
        return Everhood2Item(name, item.type, item.code, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice([x for x in misc_items.keys()])

    def create_items(self) -> None:
        soul_weapons = ["Red Soul Axe", "Green Soul Spear", "Blue Soul Knives"]
        self.random.shuffle(soul_weapons)
        
        item_collection = []
        valid_types = self.valid_location_types()
        for location in self.get_locations():
            if location.address is None:
                continue
            
            data = all_locations[location.name]
            if data.type in valid_types:
                if data.item_name == "Soul Weapon":
                    item_collection.append(self.create_item(soul_weapons.pop()))
                else:
                    item_collection.append(self.create_item(data.item_name))
        
        item_count = len(item_collection)
        act_number = self.get_act_number()
        
        if self.options.door_keys.value:
            for key, item in door_randomizer_keys.items():
                if item.act > act_number:
                    continue
                
                if key == "Neon Forest Key" and self.options.soul_color.value == self.options.soul_color.option_Blue:
                    self.push_precollected(self.create_item(key))
                elif key == "Progressive Marzian Key":
                    if self.options.soul_color.value == self.options.soul_color.option_Green:
                        self.push_precollected(self.create_item(key))
                    else:
                        item_collection.append(self.create_item(key))
                    item_collection.append(self.create_item(key))
                    item_collection.append(self.create_item(key))
                elif key == "Eternal War Key" and self.options.soul_color.value == self.options.soul_color.option_Red:
                    self.push_precollected(self.create_item(key))
                else:
                    item_collection.append(self.create_item(key))
                        

        if self.options.colorsanity.value:
            for c in colors.keys():
                if name_to_color[c] == Color.blue and self.options.soul_color.value == self.options.soul_color.option_Blue:
                    self.push_precollected(self.create_item(c))
                elif name_to_color[c] == Color.red and self.options.soul_color.value == self.options.soul_color.option_Red:
                    self.push_precollected(self.create_item(c))
                elif name_to_color[c] == Color.green and self.options.soul_color.value == self.options.soul_color.option_Green:
                    self.push_precollected(self.create_item(c))
                else:
                    item_collection.append(self.create_item(c))
           
        # At this point in time, the extra keys need to replace xp. We have a ton of 50xp available so lets replace those.
        xp_removal_count = len(item_collection) - item_count
        removed = 0

        xps = ["50xp", "0xp", "2xp", "5xp"]       
        for xp in xps:
            if removed >= xp_removal_count:
                continue

            original_collection = item_collection
            item_collection = []
            while len(original_collection) > 0:
                item = original_collection.pop()
                if item.name == xp and removed < xp_removal_count:
                    removed += 1
                    continue
                item_collection.append(item)
        
        for item in item_collection:
            self.multiworld.itempool.append(item)

    def create_regions(self) -> None:
        valid_types = self.valid_location_types()
        created_regions = {x: Region(x, self.player, self.multiworld) for x, y in region_data_table.items() if y.include_type in valid_types}

        for region_name, region_data in region_data_table.items():
            if not region_data.include_type in valid_types:
                continue
            
            region = created_regions[region_name]
            self.multiworld.regions.append(region)
            
            for data in region_data.connecting_regions:
                connection = created_regions.get(data.connect_to)
                if connection is not None:
                    region.connect(connection, data.entrance_name)
        
        for location_name, location_data in all_locations.items():
            if not location_data.type in valid_types:
                continue
                
            region = created_regions[location_data.region]
            region.add_locations({location_name: location_data.code}, Everhood2Location)

        setup_act_rules(self, self.valid_location_types(), self.options.colorsanity.value != 0, self.options.goal_condition.value)

    def valid_location_types(self) -> LocationType:
        valid_types = LocationType.item

        if self.options.cosmetics.value:
            valid_types |= LocationType.cosmetic
            
        if self.options.battle_rewards.value == self.options.battle_rewards.option_All:
            valid_types |= LocationType.major_battle
            valid_types |= LocationType.unique_battle
            valid_types |= LocationType.trash_battle
        elif self.options.battle_rewards.value == self.options.battle_rewards.option_Unique:
            valid_types |= LocationType.major_battle
            valid_types |= LocationType.unique_battle
        elif self.options.battle_rewards.value == self.options.battle_rewards.option_Major:
            valid_types |= LocationType.major_battle

        if self.options.hillbert_hotel.value:
            valid_types |= LocationType.hillbert

        if self.options.door_keys.value:
            valid_types |= LocationType.pre_dragon_doors
            
        if self.options.goal_condition.value >= self.options.goal_condition.option_Judge_Creation:
            valid_types |= LocationType.act_2

        if self.options.goal_condition.value >= self.options.goal_condition.option_Riley:
            valid_types |= LocationType.act_3

        if self.options.goal_condition.value >= self.options.goal_condition.option_Cat_Gods_Hairball:
            valid_types |= LocationType.post_game
            
        return valid_types

    def set_rules(self) -> None:
        set_everhood2_rules(self, self.valid_location_types(), self.options.door_keys.value != 0, self.options.colorsanity.value != 0,
                            self.options.soul_color.value == self.options.soul_color.option_Red, self.options.goal_condition.value) 
        
    def get_dragon_gem_count(self, valid_types: LocationType) -> int:
        # Todo: Auto Count locations and save?
        gem_count = 3 
        if LocationType.hillbert in valid_types:
            gem_count += 2
        if LocationType.pre_dragon_doors in valid_types:
            gem_count += 9
            
        return gem_count
    
    def get_needed_dragon_gem_count(self, valid_types: LocationType) -> int:
        multiplier = self.options.dragon_gems.value / 100.0
        gem_count = self.get_dragon_gem_count(valid_types)
        return max(1, floor(gem_count * multiplier))
    
    def get_act_number(self) -> int:
        return self.options.goal_condition.value
    
    def create_victory_event(self, region_name: str) -> None:
        region = self.get_region(region_name)
        location = Everhood2Location(self.player, "Victory", None, region)
        location.place_locked_item(Everhood2Item("Victory", ItemClassification.progression, None, self.player))
        region.locations.append(location)
        

    def fill_slot_data(self):
        valid_types = self.valid_location_types()
        return {
            "DragonGems": self.get_needed_dragon_gem_count(valid_types),
            "SoulColor": self.options.soul_color.value,
            "DoorKeys": self.options.door_keys.value != 0,
            "Colorsanity": self.options.colorsanity.value != 0,
            "PreventDragon": self.options.prevent_dragon.value != 0,
            "HealthMultiplier": self.options.health_multiplier.value,
            "Goal": self.options.goal_condition.value,
        }
