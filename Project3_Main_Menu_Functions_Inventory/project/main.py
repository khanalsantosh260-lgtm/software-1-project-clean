def explore():
    print("You explore the forest.")
    print("You find a small path between the trees.")


def collect_item(inventory):
    item = input("Enter item to collect: ")
    inventory.append(item)
    print(item, "was added to your inventory.")


def show_inventory(inventory):
    print("Your inventory:")

    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for item in inventory:
            print("-", item)


def rest():
    print("You rest for a while and feel better.")


name = input("Enter player name: ")
age = int(input("Enter player age: "))

inventory = []

if age < 12:
    print("You are a minor.")
    print("Game closed.")

else:
    print("Hello", name)
    print("Welcome to Forest Adventure!")

    command = ""

    while command != "lopeta":

        print()
        print("MAIN MENU")
        print("1 - Explore forest")
        print("2 - Collect item")
        print("3 - Show inventory")
        print("4 - Rest")
        print("lopeta - Quit game")

        command = input("Enter command: ")

        if command == "1":
            explore()

        elif command == "2":
            collect_item(inventory)

        elif command == "3":
            show_inventory(inventory)

        elif command == "4":
            rest()

        elif command == "lopeta":
            print("Goodbye", name)

        else:
            print("Unknown command.")