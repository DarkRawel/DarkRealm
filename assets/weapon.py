from player import Player

class Weapon:
    def __init__(self, name):
        self.name = name
    
    def damage(self):
        weapon = {
            "sword": {
                "short_sword": {
                    "stab": {"damage": 4 + self.level, "type": "piercing"},
                    "slash": {"damage": 3 + self.level, "type": "slashing"}
                },
                "long_sword": {
                    "stab": {"damage": 6 + self.level, "type": "piercing"},
                    "slash": {"damage": 5 + self.level, "type": "slashing"}  
                }
            },
            "staff": {
                "broken_staff": {
                    "burst_of_fire": {"damage": 4 + self.level, "type": "fire"},
                    "lesser_heal": {"heal": 2 + self.level, "type": "health_regeneration"}
                },
                "wooden_staff": {
                    "fire_ball": {"damage": 7 + self.level, "type": "fire"},
                    "great_heal": {"heal": 4 + self.level, "type": "health_regeneration"}
                }
            },
            "knife": {
                "small_blade": {
                    "stab": {"damage": 3 + self.level, "type": "piercing"},
                    "trow": {"damage": 4 + self.level, "type": "piercing"}
                },
                "medium_blade":{
                    "stab": {"damage": 3 + self.level, "type": "piercing"},
                    "slash": {"damage": 4 + self.level, "type": "slashing"}
                }
            },
            "instrument": {
                "flute": {
                    "strike": {"damage": 3 + self.level, "type": "bludgeon"},
                    "play": {"damage_up": 1 + self.level, "type": "damage_up"}
                },
            "guitar": {
                "strike": {"damage": 5 + self.level, "type": "bludgeon"},
                "play": {"damage_up": 3 + self.level, "type": "damage_up"}
                }
            },
        }