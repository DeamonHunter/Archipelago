from . import Everhood2TestBase

class TestAllRedSettings(Everhood2TestBase):
    options = {
        "soul_color": "Red",
        "door_keys": True,
        "dragon_gems": 100,
        "cosmetics": True,
        "battle_rewards": "All",
        "hillbert_hotel": True,
    }
    
class TestAllGreenSettings(Everhood2TestBase):
    options = {
        "soul_color": "Green",
        "door_keys": True,
        "dragon_gems": 100,
        "cosmetics": True,
        "battle_rewards": "All",
        "hillbert_hotel": True,
    }
    
class TestAllBlueSettings(Everhood2TestBase):
    options = {
        "soul_color": "Blue",
        "door_keys": True,
        "dragon_gems": 100,
        "cosmetics": True,
        "battle_rewards": "All",
        "hillbert_hotel": True,
    }