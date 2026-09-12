name = input("Enter player name: ")
age = int(input("Enter player age: "))

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
        print("2 - Rest")
        print("3 - Check status")
        print("lopeta - Quit game")

        command = input("Enter command: ")

        if command == "1":
            print("You walk into the forest and see tall trees.")

        elif command == "2":
            print("You sit near a tree and take a rest.")

        elif command == "3":
            print("You are safe and ready to continue.")

        elif command == "lopeta":
            print("Goodbye", name)

        else:
            print("Unknown command.")