import random

class Enemies:
    def __init__(self, name):
        self.name = name
        self.health = self.set_enemies_health(name)

    def set_enemies_health(self, name):
        enemies_health = {
            "skeleton": 17 + random.randint(1, 16),
            "zombie": 22 + random.randint(1, 24),
            "goblin": 9 + random.randint(1, 12),
            "dragon": 150 + random.randint(1, 25)
        }
        return enemies_health.get(name, 10)
    
    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)
        print(f"{self.name} takes {amount} damage. Health: {self.health}")
        if self.health == 0:
            print(f"{self.name} has been defeated!")

    @property
    def is_alive(self):
        return self.health > 0
