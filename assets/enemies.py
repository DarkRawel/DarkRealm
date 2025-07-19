import random

from player import Player

class Enemies:
    def __init__(self, name, e_level):
        self.name = name
        self.health = self.set_enemies_health(name)
        self.e_level = e_level + self.level

    def set_enemies_health(self, name):
        enemies_health = {
            "skeleton": 17 + random.randint(1, 16) + self.e_level,
            "zombie": 22 + random.randint(1, 24) + self.e_level,
            "goblin": 9 + random.randint(1, 12) + self.e_level,
            "dragon": 150 + random.randint(1, 25) + self.e_level
        }
        return enemies_health.get(name, 10)
    
    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)
        print(f"{self.name} takes {amount} damage. Health: {self.health}")
        if self.health == 0:
            print(f"{self.name} has been defeated!")

    def set_attack_power(self, name):
        attack_power = {
            "skeleton": 5 + random.randint(1, 4) + self.e_level,
            "zombie": 7 + random.randint(1, 6) + self.e_level,
            "goblin": 4 + random.randint(1, 3) + self.e_level,
            "dragon": 20 + random.randint(5, 10) + self.e_level
        }
        return attack_power.get(name, 2)

    @property
    def is_alive(self):
        return self.health > 0
