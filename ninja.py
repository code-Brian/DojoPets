import pet

class Ninja:
    # implement 
    def __init__(self,first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        # self.pet = pet.Pet()
    
    # implement methods here
    def walk(self):
        # walks the ninja's pet invoking the pet play() method
        # self.Pet.play()
        return self
    def feed(self):
        # feeds the ninja's pet invoking the pet feed() method
        print("This will feed the pet, eventually.")
    def bathe(self):
        # cleans the ninja's pet invoking the pet noise() method
        print("This will clean the pet, eventually.")