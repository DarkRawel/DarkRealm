class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"{item} added to inventory.")

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from inventory.")
        else:
            print(f"{item} is not in your inventory.")

    def list(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in self.items:
                print(f" - {item}")