# enemies

import random

from player import Player

class Enemies:
    def __init__(self, name, e_level):
        self.name = name
        self.e_level = e_level
        self.health = self.set_enemies_health(name)
        self.e_level = e_level + self.level

    def set_enemies_health(self, name):
        enemies_health = {
            "skeleton": 17 + random.randint(1, 16) + self.e_level,
            "zombie": 22 + random.randint(1, 24) + self.e_level,
            "goblin": 9 + random.randint(1, 12) + self.e_level,
            "dragon": 150 + random.randint(15, 25) + self.e_level
        }
        return enemies_health.get(name, 10)
    
    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)
        print(f"{self.name} takes {amount} damage. Health: {self.health}")
        if self.health == 0:
            print(f"{self.name} has been defeated!")

    def set_attack_power(self, name):
        attack_power = {
            "skeleton": {
                "bow": {
                    "arrow_shot": {"damage": 5 + random.randint(1, 4) + self.e_level, "type": "piercing"}
                },
                "sword": {
                    "slash": {"damage": 7 + random.randint(1, 2) + self.e_level, "type": "slashing"}
                }
            },
            "zombie": {
                "unarmed": {
                    "claw": {"damage": 7 + random.randint(1, 6) + self.e_level, "type": "slashing"}
                },
                "sword": {
                    "slash": {"damage": 8 + random.randint(1, 3) + self.e_level, "type": "slashing"}
                }
            },
            "goblin": {
                "small_blade": {
                    "slash": {"damage": 4 + random.randint(1, 3) + self.e_level, "type": "slashing"}
                },
                "mace": {
                    "strike": {"damage": 5 + random.randint(1, 3) + self.e_level, "type": "bludgeon"}
                }
            },
            "dragon": {
                "magic": {
                    "fire_breath": {"damage": 20 + random.randint(5, 10) + self.e_level, "type": "fire"},
                    "ice_breath": {"damage": 20 + random.randint(5, 10) + self.e_level, "type": "ice"}
                },
                "fyzical": {
                    "claw": {"damage": 20 + random.randint(5, 10) + self.e_level, "type": "slashing"},
                    "roar": {"damage": 5 + random.randint(1, 5) + self.e_level, "type": "debuff"}
                }
            }
        }
        return attack_power.get(name, {})

    @property
    def is_alive(self):
        return self.health > 0
