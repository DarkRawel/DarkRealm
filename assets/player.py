from inventory import Inventory

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.health = self.set_class_health(player_class)
        self.gold = 0
        self.level = 1
        self.experience = 0
        self.inventory = Inventory()

    def set_class_health(self, player_class):
        class_health = {
            'wizard': 90,
            'fighter': 120,
            'rogue': 100,
            'Bard': 90

        }
        return class_health.get(player_class.lower(), 100)

    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)
        print(f"{self.name} takes {amount} damage. Health: {self.health}")

    def show_status(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.player_class}")
        print(f"HP: {self.health}")
        print(f"Level: {self.level}")
        print(f"Inventory: {', '.join(self.inventory.items) or 'Empty'}")
