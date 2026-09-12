from item import Item
from room import Room
from player import Player


apple = Item("Apple", 0.2)
key = Item("Key", 0.1)
sword = Item("Sword", 2.5)

forest = Room("Forest", apple)
cave = Room("Cave", key)
castle = Room("Castle", sword)

rooms = [forest, cave, castle]

name = input("Enter player name: ")
age = int(input("Enter player age: "))

if age < 12:
    print("You are a minor.")
    print("Game closed.")

else:
    player = Player(name, forest)

    print("Hello", player.name)
    print("Welcome to Forest Adventure!")

    command = ""

    while command != "lopeta":

        print()
        print("MAIN MENU")
        print("1 - Show location")
        print("2 - Move")
        print("3 - Collect item")
        print("4 - Show inventory")
        print("lopeta - Quit game")

        command = input("Enter command: ")

        if command == "1":
            print("You are in", player.location.name)

            if player.location.item is not None:
                print("There is an item here:", player.location.item.name)
            else:
                print("There is no item here.")

        elif command == "2":
            print("Choose where to move:")
            print("1 - Forest")
            print("2 - Cave")
            print("3 - Castle")

            choice = input("Enter place number: ")

            if choice == "1":
                player.move(forest)
            elif choice == "2":
                player.move(cave)
            elif choice == "3":
                player.move(castle)
            else:
                print("Unknown place.")

        elif command == "3":
            player.collect_item()

        elif command == "4":
            player.show_inventory()

        elif command == "lopeta":
            print("Goodbye", player.name)

        else:
            print("Unknown command.")