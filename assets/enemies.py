class Enemies:
    def __init__(self, name, health):
        self.name = name
        self.health = self.set_enemies_health(name)

        def set_enemies_health(self):
            enemies_health = {
                "skeleton": 100,
            }