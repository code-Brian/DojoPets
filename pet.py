class Pet:
    # ! Class Attributes
    health = 100
    energy = 100

    # implement the following attributes with the constructor/initializer
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

    def add_health(self,health):
        self.health = self.health + health
        print(f"{self.name}'s health was increased to {self.health}")
        return self

    def add_energy(self,energy):
        self.energy = self.energy + energy
        print(f"{self.name}'s energy was increased to {self.energy}")
        return self

    def sleep(self):
        # increases the pet's energy by 25
        print(f"{self.name} went to sleep.")
        self.add_energy(25)
        return self

    def eat(self):
        # increases the pet's energy by 5 and health by 10.
        print(f"{self.name} ate some food.")
        self.add_energy(5)
        self.add_health(10)
        return self

    def play(self):
        # increases the pet's health by 5.
        print(f"{self.name} got to play!")
        self.add_health(5)
        return self

    def noise(self, sound):
        # prints out the pet's sound
        print(f"{self.name} says: {sound}")