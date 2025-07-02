from Options import Toggle, Choice, OptionSet, PerGameCommonOptions, OptionGroup, Range
from dataclasses import dataclass
from .Locations import battle_locations


class DoorKeys(Toggle):
    """
    Blocks the ability to enter doors without the corresponding key. Adds additional checks for completing routes for these door.
    """
    display_name = "Door Keys"
    default = True

    
class SoulColor(Choice):
    """
    Determines which soul color the player will be when the run is started. If combined with Door Keys, the starting route's key will be given to you.
    """
    display_name = "Soul Color"
    default = 1
    option_Blue = 1
    option_Green = 2
    option_Red = 3


class Colorsanity(Toggle):
    """
    When enabled, you can only reflect colors that have been given to you. By default, you start with your soul color.
    """
    display_name = "Colorsanity"


class DragonPowerGemPercentage(Range):
    """
    Determines the percentage of gems required to beat the dragon.
    """
    display_name = "Dragon's Power Gem Requirement"
    range_start = 1
    range_end = 100
    default = 75


class RandomizeCosmetics(Toggle):
    """
    Add cosmetics and their locations to the pool.
    """
    display_name = "Cosmetics"


class HillbertHotel(Toggle):
    """
    Whether to include the Hillbert Hotel and its rooms, keys, battles and items to the pool.
    
    If Battle Rewards is enabled, Hillbert Hotel battles will be included.
    """
    display_name = "Include Hillbert Hotel"


class RandomizeBattleRewards(Choice):
    """
    Chooses what battles will be added to the randomization. Their Battles and xps will be added.
    - Major Battles: Unique Battles which are fought on the main path of any route.
    - Unique Battles: Battles which feature a unique character.
    - All Battles: All non-spaceship battles.
    """
    display_name = "Battle Rewards"
    default = 1    
    option_None = 0
    option_Major = 1
    option_Unique = 2
    option_All = 3


# class Colloseum(Toggle):
#     """
#     Whether to include the Colloseum and its battles to the pool. Does nothing without Battles
#     """
#     display_name = "Include Colloseum"


# class BattleRandomisation(Choice):
#     """
#     Randomises which battles get placed at locations.
#     - Within Categories: Enemies will randomise within their group. So Minor Battles with Minor Battles etc.
#     - Anywhere: Enemies can appear anywhere.
#     """
#     display = "Enemizer"
#     option_None = 0
#     option_WithinCategories = 1
#     option_Anywhere = 2


# class ExcludeFromEnemizer(OptionSet):
#     """
#     Chooses which battles will be forced to stay on their location.
#     """
#     display = "Exclude From Enemizer"
#     valid_keys = battle_locations.keys()
#     # default = ["Riley Battle", "Cat God's Hairball Battle", "Dragon 1 Battle", "Dragon 2 Battle", "Angry Shade Battle"]


everhood2_option_groups = [
    OptionGroup("Setup", [
        SoulColor, # Todo: Add this to a different category with difficulty options
        DragonPowerGemPercentage
    ]),
    OptionGroup("Features", [
        DoorKeys,
        Colorsanity,
    ]),
    OptionGroup("Randomisation", [
        RandomizeCosmetics,
        RandomizeBattleRewards,
        HillbertHotel,
        # Colloseum,
    ]),
    # OptionGroup("Enemizer", [
    #     BattleRandomisation,
    #     ExcludeFromEnemizer
    # ]),
]


@dataclass
class Everhood2Options(PerGameCommonOptions):
    soul_color: SoulColor
    door_keys: DoorKeys
    dragon_gems: DragonPowerGemPercentage
    cosmetics: RandomizeCosmetics
    battle_rewards: RandomizeBattleRewards
    hillbert_hotel: HillbertHotel
    colorsanity: Colorsanity
    # colloseum: Colloseum
    # Enemizer: BattleRandomisation
    # Enemizer_exclude: ExcludeFromEnemizer
