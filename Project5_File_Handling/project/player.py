class Player:
    def __init__(self, name, location):
        self.name = name
        self.items = []
        self.location = location

    def move(self, destination):
        self.location = destination
        print("You moved to", self.location.name)

    def collect_item(self):
        if self.location.item is not None:
            self.items.append(self.location.item)
            print("You collected", self.location.item.name)
            self.location.item = None
        else:
            print("There is no item in this room.")

    def show_inventory(self):
        print("Your inventory:")

        if len(self.items) == 0:
            print("Inventory is empty.")
        else:
            for item in self.items:
                print("-", item.name, item.weight, "kg")