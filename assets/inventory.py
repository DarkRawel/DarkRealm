# inventory

class Inventory:
    def __init__(self, max_items=10):
        self.max_items = max_items
        self.items = {
            'weapons': {},
            'consumables': {},
            'quest_items': {}
        }

    def add(self, category, item, quantity=1):
        if category not in self.items:
            print(f"Invalid category: {category}")
            return

        if self.total_items() + quantity > self.max_items:
            print("Inventory is full!")
            return

        if item in self.items[category]:
            self.items[category][item] += quantity
        else:
            self.items[category][item] = quantity

        print(f"{quantity}x {item} added to {category}.")

    def remove(self, category, item, quantity=1):
        if category not in self.items or item not in self.items[category]:
            print(f"{item} not found in {category}.")
            return

        if self.items[category][item] <= quantity:
            del self.items[category][item]
            print(f"{item} removed from {category}.")
        else:
            self.items[category][item] -= quantity
            print(f"{quantity}x {item} removed from {category}.")

    def list(self):
        if self.total_items() == 0:
            print("Inventory is empty.")
            return

        print("Inventory:")
        for category, contents in self.items.items():
            if contents:
                print(f" {category.capitalize()}:")
                for item, qty in contents.items():
                    print(f"   - {item} x{qty}")

    def total_items(self):
        return sum(
            qty for category in self.items.values()
            for qty in category.values()
        )

    def clear(self):
        for category in self.items:
            self.items[category] = {}
        print("Inventory cleared.")

    def has(self, category, item):
        return item in self.items.get(category, {})