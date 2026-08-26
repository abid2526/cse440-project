class Player:
    def __init__(self):
        self.health = 100
        self.gold = 30
        self.weapon = False
        self.reputation = "Good"
        self.location = "Village"
        self.crystal = False

    def status(self):
        return (
            f"Health: {self.health}\n"
            f"Gold: {self.gold}\n"
            f"Weapon: {'Yes' if self.weapon else 'No'}\n"
            f"Reputation: {self.reputation}\n"
            f"Location: {self.location}"
        )

    def is_alive(self):
        return self.health > 0