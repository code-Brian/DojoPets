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
        print("The pet is sleeping and its health is increased by 25")

    def eat(self):
        # increases the pet's energy by 5 and health by 10. 
        print("The pet is eating and its energy is increased by 5 and health is increased by 10")

    def play(self):
        # increases the pet's health by 5.
        print("The pet is playing and its health is increased by 5")

    def noise(self):
        # prints out the pet's sound
        print("The pet is making its sound! Aww! How cute!")