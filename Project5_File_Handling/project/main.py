import os

from item import Item
from room import Room
from player import Player


folder = os.path.dirname(__file__)


def read_text_file(file_name):
    file_path = os.path.join(folder, file_name)

    file = open(file_path, "r", encoding="utf-8")
    text = file.read()
    file.close()

    print(text)


def create_world():
    apple = Item("Apple", 0.2)
    key = Item("Key", 0.1)
    sword = Item("Sword", 2.5)

    forest = Room("Forest", apple)
    cave = Room("Cave", key)
    castle = Room("Castle", sword)

    rooms = [forest, cave, castle]

    return rooms


def find_room(rooms, room_name):
    for room in rooms:
        if room.name == room_name:
            return room

    return rooms[0]


def make_item(item_name):
    if item_name == "Apple":
        return Item("Apple", 0.2)
    elif item_name == "Key":
        return Item("Key", 0.1)
    elif item_name == "Sword":
        return Item("Sword", 2.5)
    else:
        return Item(item_name, 0)


def remove_collected_items_from_rooms(rooms, inventory):
    for item in inventory:
        for room in rooms:
            if room.item is not None and room.item.name == item.name:
                room.item = None


def save_game(player):
    file_name = "save_" + player.name + ".txt"
    file_path = os.path.join(folder, file_name)

    file = open(file_path, "w", encoding="utf-8")

    file.write(player.name + "\n")
    file.write(player.location.name + "\n")

    item_names = []

    for item in player.items:
        item_names.append(item.name)

    file.write(",".join(item_names) + "\n")

    file.close()

    print("Game saved.")


def load_game(rooms):
    name = input("Enter player name for saved game: ")
    file_name = "save_" + name + ".txt"
    file_path = os.path.join(folder, file_name)

    if os.path.exists(file_path):
        file = open(file_path, "r", encoding="utf-8")

        saved_name = file.readline().strip()
        saved_location = file.readline().strip()
        saved_items = file.readline().strip()

        file.close()

        location = find_room(rooms, saved_location)
        player = Player(saved_name, location)

        if saved_items != "":
            item_names = saved_items.split(",")

            for item_name in item_names:
                player.items.append(make_item(item_name))

        remove_collected_items_from_rooms(rooms, player.items)

        print("Game loaded.")
        return player

    else:
        print("Saved game was not found.")
        return None


def start_new_game(rooms):
    name = input("Enter player name: ")
    age = int(input("Enter player age: "))

    if age < 12:
        print("You are a minor.")
        print("Game closed.")
        return None

    player = Player(name, rooms[0])
    return player


rooms = create_world()

read_text_file("intro.txt")
read_text_file("instructions.txt")

choice = input("Do you want to continue a saved game? yes/no: ")

if choice == "yes":
    player = load_game(rooms)

    if player is None:
        player = start_new_game(rooms)

else:
    player = start_new_game(rooms)


if player is not None:
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
        print("5 - Save game")
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
                player.move(rooms[0])
            elif choice == "2":
                player.move(rooms[1])
            elif choice == "3":
                player.move(rooms[2])
            else:
                print("Unknown place.")

        elif command == "3":
            player.collect_item()

        elif command == "4":
            player.show_inventory()

        elif command == "5":
            save_game(player)

        elif command == "lopeta":
            print("Goodbye", player.name)

        else:
            print("Unknown command.")