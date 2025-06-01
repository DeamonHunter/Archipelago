from worlds.AutoWorld import World, WebWorld
from BaseClasses import Region, Item, Tutorial
from typing import ClassVar, Type
from Options import PerGameCommonOptions

from .Options import Everhood2Options, everhood2_option_groups
from .Items import Everhood2Item, all_items, item_groups, misc_items
from .Locations import Everhood2Location, all_locations, LocationType
from .Regions import region_data_table
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

    def create_item(self, name: str) -> Item:
        item = all_items[name]
        return Everhood2Item(name, item.type, item.code, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice([x for x in misc_items.keys()])

    def create_items(self) -> None:
        valid_types = self.valid_location_types()
        for location in self.multiworld.get_locations(self.player):
            data = all_locations[location.name]
            if data.type in valid_types:
                self.multiworld.itempool.append(self.create_item(data.item_name))

    def create_regions(self) -> None:
        valid_types = self.valid_location_types()
        created_regions = {x: Region(x, self.player, self.multiworld) for x, y in region_data_table.items() if y.include_type in valid_types}

        for region_name, region_data in region_data_table.items():
            if not region_data.include_type in valid_types:
                continue
            
            region = created_regions[region_name]
            self.multiworld.regions.append(region)
            
            for name in region_data.connecting_regions:
                connection = created_regions.get(name)
                if connection is not None:
                    region.connect(connection)
        
        for location_name, location_data in all_locations.items():
            if not location_data.type in valid_types:
                continue
                
            region = created_regions[location_data.region]
            region.add_locations({location_name: location_data.code}, Everhood2Location)

    def valid_location_types(self) -> set[LocationType]:
        valid_types = { LocationType.item }
        if self.options.cosmetics.value:
            valid_types.add(LocationType.cosmetic)
        if self.options.battle_rewards.value == self.options.battle_rewards.option_Minor:
            valid_types.add(LocationType.major_battle)
            valid_types.add(LocationType.trash_battle)
        elif self.options.battle_rewards.value == self.options.battle_rewards.option_Major:
            valid_types.add(LocationType.major_battle)

        if self.options.hillbert_hotel.value:
            valid_types.add(LocationType.hillbert_item)
            if LocationType.cosmetic in valid_types:
                valid_types.add(LocationType.hillbert_cosmetic)
            if LocationType.major_battle in valid_types:
                valid_types.add(LocationType.hillbert_battle)

        return valid_types

    def set_rules(self) -> None:
        valid_types = self.valid_location_types()
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Power Gem", self.player, 3)
        
        if LocationType.hillbert_item in valid_types:
            self.get_entrance("Hillbert Hotel -> Floor 23").access_rule = lambda state: state.has("Floor 23 Key", self.player)
            self.get_location("Floor 23 Complete Chest").access_rule = lambda state: state.has("Floor 23 Key", self.player)
            
            self.get_entrance("Hillbert Hotel -> Floor Gold").access_rule = lambda state: state.has("Gold Key", self.player)
            self.get_location("Floor Gold Complete Chest").access_rule = lambda state: state.has("Gold Key", self.player)
            
            if LocationType.hillbert_cosmetic in valid_types:
                self.get_location("Cat Ears").access_rule = lambda state: state.has("Floor 23 Key", self.player)
                self.get_location("Cat Ears Bald").access_rule = lambda state: state.has("Floor 23 Key", self.player)
                self.get_location("Oingo Boingo").access_rule = lambda state: state.has("Gold Key", self.player)  

    def fill_slot_data(self):
        return {
            # "victoryLocation": self.victory_song_name,
            # "deathLink": self.options.death_link.value,
            # "musicSheetWinCount": self.get_music_sheet_win_count(),
            # "gradeNeeded": self.options.grade_needed.value,
        }
