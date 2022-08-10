class Pet:
    # ! Class Attributes
    health = 100
    energy = 100

    # implement the following attributes with the constructor/initializer
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

    # implement the following methods:
    def sleep(self):
        # increases the pet's energy by 25
        previous_energy = self.energy
        self.energy = self.energy + 25
        print(f"{self.name}'s energy was at {previous_energy}. After resting, energy is now at {self.energy}")
        return self

    def eat(self):
        # increases the pet's energy by 5 and health by 10. 
        previous_energy = self.energy
        previous_health = self.health
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"{self.name}'s energy was {previous_energy}. Health was {previous_health}.\nAfter eating, energy is now {self.energy} and health is {self.health}")

    def play(self):
        # increases the pet's health by 5.
        previous_health = self.health
        self.health = self.health + 5
        print(f"{self.name}'s health was {previous_health}. After playing, health is now {self.health}")

    def noise(self, sound):
        # prints out the pet's sound
        print(f"{self.name} says: {sound}")