from inventory import Inventory

class Player:
    def __init__(self, name, player_class, level):
        self.name = name
        self.player_class = player_class
        self.health = self.set_class_health(player_class)
        self.gold = 0
        self.level = level
        self.experience = 0
        self.inventory = Inventory()

    def set_class_health(self, player_class):
        class_health = {
            'wizard': 40,
            'fighter': 70,
            'rogue': 60,
            'bard': 50
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

    @property
    def is_alive(self):
        return self.health > 0

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.health += 10
        print(f"{self.name} leveled up! Level: {self.level}, HP: {self.health}")
