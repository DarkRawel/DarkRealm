from player import Player

class Weapon:
    def __init__(self, name):
        self.name = name
    
    def damage(self):
        player_weapon = {
            "sword": {
                "short_sword": 3 + self.level,
                "long_sword": 7 + self.level
            },
            "staff": {
                "broken_staff": 5 + self.level,
                "wooden_staff": 8 + self.level
            },
            "knife": {
                "small_blade": 4 + self.level,
                "medium_blade": 6 + self.level
            },
            "instrument": {
                "flute": 4 + self.level,
                "guitar": 5 + self.level
            }
        }