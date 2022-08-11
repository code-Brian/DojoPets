# This is where the fun begins! 

import ninja
import pet

# brian = ninja.Ninja("Brian","Denmark","Beef Jerky", "Organic Kibble", "Dog")
# print(f"Hello, {brian.first_name}! Welcome to Dojo Pets!")

first_pet = {
    "name":"Brufus",
    "type": "Dog", 
    "tricks": ["Sit", "Snuggle","Touch"],
    "sound": "Bark! Bark!"
}

second_pet = {
    "name":"Joules",
    "type": "Dog", 
    "tricks": ["Sit", "Snuggle","Touch"],
    "sound": "Awoo! Bork! Bork! Awoooooowowowooo!"
}

ninja_brian = {
    "first_name":"Brian",
    "last_name":"Denmark",
    "treats": ["kibble","bacon","blueberries"],
    "pet_food": "premium pupper chow",
}

brian = ninja.Ninja(ninja_brian, first_pet)
print(brian.ninjaPet.type)
brian.walk().feed().bathe()

joules = pet.Dog(second_pet)
joules.chase_tail()