from Options import Toggle, Choice, OptionSet, PerGameCommonOptions, OptionGroup
from dataclasses import dataclass
from .Locations import battle_locations


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
    - Major Battles: Battles which feature a unique character.
    - Minor Battles: Battles which
    """
    display_name = "Battle Rewards"
    default = 1    
    option_None = 0
    option_Major = 1
    option_Minor = 2


class Colloseum(Toggle):
    """
    Whether to include the Colloseum and its battles to the pool. Does nothing without Battles
    """
    display_name = "Include Hillbert Hotel"


class BattleRandomisation(Choice):
    """
    Randomises which battles get placed at locations.
    - Within Categories: Enemies will randomise within their group. So Minor Battles with Minor Battles etc.
    - Anywhere: Enemies can appear anywhere.
    """
    display = "Enemizer"
    option_None = 0
    option_WithinCategories = 1
    option_Anywhere = 2


class ExcludeFromEnemizer(OptionSet):
    """
    Chooses which battles will be forced to stay on their location.
    """
    display = "Exclude From Enemizer"
    valid_keys = battle_locations.keys()
    # default = ["Riley Battle", "Cat God's Hairball Battle", "Dragon 1 Battle", "Dragon 2 Battle", "Angry Shade Battle"]


everhood2_option_groups = [
    OptionGroup("Randomisation", [
        RandomizeCosmetics,
        RandomizeBattleRewards,
        HillbertHotel,
        Colloseum,
    ]),
    OptionGroup("Enemizer", [
        BattleRandomisation,
        ExcludeFromEnemizer
    ]),
]


@dataclass
class Everhood2Options(PerGameCommonOptions):
    cosmetics: RandomizeCosmetics
    battle_rewards: RandomizeBattleRewards
    hillbert_hotel: HillbertHotel
    colloseum: Colloseum
    Enemizer: BattleRandomisation
    Enemizer_exclude: ExcludeFromEnemizer
