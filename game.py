import time

def slow(text, delay=0.04):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    slow("Welcome to the DarkRealm...\n")
    name = input("What is your name, adventurer? ")
    slow(f"\nAh, {name}... a name that shall echo through time.\n")
    
    print("Choose your class:")
    print("1. Warrior\n2. Mage\n3. Rogue")
    choice = input("> ")

    if choice == "1":
        player_class = "Warrior"
    elif choice == "2":
        player_class = "Mage"
    elif choice == "3":
        player_class = "Rogue"
    else:
        player_class = "Peasant"

    slow(f"\nYou are now a {player_class} of the DarkRealm...\n")
    first_scene(name, player_class)

def first_scene(name, player_class):
    slow("You awaken in a dark forest, the smell of ash and blood in the air.")
    slow("A path splits ahead of you.")
    print("Do you:")
    print("1. Take the left path toward the light.")
    print("2. Take the right path into the mist.")
    path = input("> ")

    if path == "1":
        slow("You walk toward the light... but something watches you.")
        slow("A nice clearing with a small pond stands in front of you.")
        slow("But the feeling doesn't stop.")

    elif path == "2":
        slow("The mist swallows you whole. Shadows move in silence.")
        slow("Suddenly something runs towards you.")

    else:
        slow("You stand still for too long... and the forest claims you.")

if __name__ == "__main__":
    intro()
