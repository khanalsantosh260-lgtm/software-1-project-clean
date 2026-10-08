import os

from item import Item
from room import Room
from player import Player


folder = os.path.dirname(__file__)


def read_text_file(file_name):
    file_path = os.path.join(folder, file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    print(text)


def create_world():
    tools = Item("Tools", 2.0)
    filter_part = Item("Filter part", 0.5)

    forest = Room("Forest", tools)
    cave = Room("Cave", filter_part)
    castle = Room("Castle", None)

    return [forest, cave, castle]


def find_room(rooms, room_name):
    for room in rooms:
        if room.name == room_name:
            return room

    return rooms[0]


def make_item(item_name):
    if item_name == "Tools":
        return Item("Tools", 2.0)
    elif item_name == "Filter part":
        return Item("Filter part", 0.5)
    else:
        return Item(item_name, 0)


def remove_collected_items_from_rooms(rooms, inventory):
    for item in inventory:
        for room in rooms:
            if room.item is not None:
                if room.item.name == item.name:
                    room.item = None


def get_save_path(name):
    safe_name = ""

    for character in name:
        if character.isalnum() or character in "_-":
            safe_name += character

    if safe_name == "":
        safe_name = "player"

    return os.path.join(folder, "save_" + safe_name + ".txt")


def save_game(player):
    file_path = get_save_path(player.name)

    item_names = []

    for item in player.items:
        item_names.append(item.name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(player.name + "\n")
        file.write(player.location.name + "\n")
        file.write(",".join(item_names) + "\n")
        file.write(",".join(player.cleaned_locations) + "\n")
        file.write(str(player.has_evidence) + "\n")
        file.write(",".join(player.supporting_groups) + "\n")

    print("Game saved.")


def load_game(rooms):
    name = input("Enter player name for saved game: ").strip()
    file_path = get_save_path(name)

    if not os.path.exists(file_path):
        print("Saved game was not found.")
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        saved_name = file.readline().strip()
        saved_location = file.readline().strip()
        saved_items = file.readline().strip()
        saved_cleaned_locations = file.readline().strip()
        saved_evidence = file.readline().strip()
        saved_supporting_groups = file.readline().strip()

    location = find_room(rooms, saved_location)
    player = Player(saved_name, location)

    if saved_items != "":
        for item_name in saved_items.split(","):
            player.items.append(make_item(item_name))

    if saved_cleaned_locations != "":
        player.cleaned_locations = saved_cleaned_locations.split(",")

    player.has_evidence = saved_evidence == "True"

    if saved_supporting_groups != "":
        player.supporting_groups = saved_supporting_groups.split(",")

    remove_collected_items_from_rooms(rooms, player.items)

    print("Game loaded.")
    return player


def start_new_game(rooms):
    name = input("Enter player name: ").strip()

    while name == "":
        name = input("Please enter a name: ").strip()

    while True:
        try:
            age = int(input("Enter player age: "))

            if age < 0:
                print("Age cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a whole number.")

    print("Welcome,", name)
    print("Your age is", age)

    return Player(name, rooms[0])


def has_item(player, item_name):
    for item in player.items:
        if item.name == item_name:
            return True

    return False


def attempt_repair(player):
    if player.location.name != "Castle":
        print("The water filter is at the Castle.")
        print("Go there to attempt the repair.")
        return False

    if not has_item(player, "Tools"):
        print("You need tools from the Forest.")
        return False

    if not has_item(player, "Filter part"):
        print("You need a filter part from the Cave.")
        return False

    print()
    print("You use the tools to install the filter part.")
    print("The repaired filter provides clean water to the village!")
    print("YOU WIN!")
    return True


def attempt_disposal(player):
    if player.location.name != "Castle":
        print("Take the collected rubbish to the Castle.")
        return False

    required_locations = ["Forest", "Cave", "Castle"]

    for location_name in required_locations:
        if location_name not in player.cleaned_locations:
            print("You still need to collect rubbish at", location_name)
            return False

    print()
    print("You sort the collected rubbish for proper disposal.")
    print("The village river is free of the dumped rubbish!")
    print("YOU WIN!")
    return True


def show_location(player):
    print("You are in", player.location.name)

    if player.location.item is not None:
        print("There is an item here:", player.location.item.name)
    else:
        print("There is no item here.")

    if player.location.name in player.cleaned_locations:
        print("You have already collected the rubbish here.")
    else:
        print("There is rubbish here. Choose 7 to collect it.")

    if player.location.name == "Forest":
        if player.has_evidence:
            print("You have already recorded the pollution evidence.")
        else:
            print("Choose 9 to record pollution evidence.")

    else:
        print("There are villagers here. Choose 10 to talk to them.")

    if player.location.name == "Castle":
        print("The village water filter is here.")
        print("Choose 6 to attempt a repair.")
        print("The rubbish disposal point is also here.")
        print("Choose 8 after collecting rubbish at all three locations.")


def choose_destination(player, rooms):
    print("Choose where to move:")

    for number, room in enumerate(rooms, start=1):
        print(number, "-", room.name)

    choice = input("Enter place number: ").strip()

    if choice == "1":
        player.move(rooms[0])
    elif choice == "2":
        player.move(rooms[1])
    elif choice == "3":
        player.move(rooms[2])
    else:
        print("Unknown place.")


def main():
    rooms = create_world()

    read_text_file("intro.txt")
    read_text_file("instructions.txt")

    choice = input(
        "Do you want to continue a saved game? yes/no: "
    ).strip().lower()

    while choice not in ["yes", "no"]:
        choice = input("Please enter yes or no: ").strip().lower()

    player = None

    if choice == "yes":
        player = load_game(rooms)

    if player is None:
        player = start_new_game(rooms)

    game_won = False

    while not game_won:
        print()
        print("MAIN MENU")
        print("1 - Show location")
        print("2 - Move")
        print("3 - Collect item")
        print("4 - Show inventory")
        print("5 - Save game")
        print("6 - Attempt water filter repair")
        print("7 - Collect rubbish")
        print("8 - Dispose of rubbish")
        print("9 - Collect pollution evidence")
        print("10 - Talk to villagers")
        print("lopeta - Quit game")

        command = input("Enter command: ").strip().lower()

        if command == "1":
            show_location(player)

        elif command == "2":
            choose_destination(player, rooms)

        elif command == "3":
            player.collect_item()

        elif command == "4":
            player.show_inventory()

        elif command == "5":
            save_game(player)

        elif command == "6":
            game_won = attempt_repair(player)

        elif command == "7":
            player.collect_rubbish()

        elif command == "8":
            game_won = attempt_disposal(player)

        elif command == "9":
            player.collect_evidence()

        elif command == "10":
            game_won = player.talk_to_villagers()

        elif command == "lopeta":
            print("Goodbye", player.name)
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()