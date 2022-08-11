import pet

class Ninja:
    # implement 
    def __init__(self, dict:dict,pet_dict:dict):
        self.first_name = dict["first_name"]
        self.last_name = dict["last_name"]
        self.treats = dict["treats"]
        self.pet_food = dict["pet_food"]
        self.ninjaPet = pet.Pet(pet_dict)
    
    # implement methods here
    def walk(self):
        # walks the ninja's pet invoking the pet play() method
        print(f"{self.first_name} took {self.ninjaPet.name} for a walk!")
        self.ninjaPet.play()
        return self

    def feed(self):
        # feeds the ninja's pet invoking the pet feed() method
        print(f"{self.first_name} fed {self.ninjaPet.name}. They're full and content now!")
        self.ninjaPet.eat()
        return self

    def bathe(self):
        # cleans the ninja's pet invoking the pet noise() method
        print(f"{self.first_name} bathed {self.ninjaPet.name}. They don't seem too happy about that.")
        self.ninjaPet.noise()

