# Created by Caren Rayon for the Python OOP Challenge

from pet import Pet

print("\n🎮 Welcome to Digital Pet Game!\n")

# Customize your pet's name here
my_pet = Pet("Zuri")

# Begin interaction
my_pet.get_status()

print("\n🍼 Feeding Zuri...")
my_pet.eat()

print("\n😴 Putting Zuri to sleep...")
my_pet.sleep()

print("\n🎾 Time to play!")
my_pet.play()

print("\n📚 Training new tricks...")
my_pet.train("roll over")
my_pet.train("high five")

print("\n🐶 Let's see all tricks:")
my_pet.show_tricks()

print("\n📊 Final Status:")
my_pet.get_status()
