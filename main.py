# This is where the fun begins! 

import ninja
import pet

brian = ninja.Ninja("Brian","Denmark","Beef Jerky", "Organic Kibble", "Dog")
print(f"Hello, {brian.first_name}! Welcome to Dojo Pets!")

first_pet = {
    "name":"Brufus",
    "type": "Dog", 
    "tricks": ["Sit", "Snuggle","Touch"] 
}
brufus = pet.Pet(first_pet)
print(f"Hey, {brufus.name}! You're so cute! Have a treat!")

brufus.sleep()
brufus.eat()
brufus.play()
brufus.noise("Bark! Bark!")