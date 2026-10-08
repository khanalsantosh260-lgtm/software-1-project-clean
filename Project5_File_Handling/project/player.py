class Player:
    def __init__(self, name, location):
        self.name = name
        self.items = []
        self.location = location
        self.cleaned_locations = []
        self.has_evidence = False
        self.supporting_groups = []

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

        print("Rubbish collected from:")

        if len(self.cleaned_locations) == 0:
            print("No locations yet.")
        else:
            for location_name in self.cleaned_locations:
                print("-", location_name)

        print("Pollution evidence collected:", self.has_evidence)

        print("Groups supporting you:")

        if len(self.supporting_groups) == 0:
            print("No groups yet.")
        else:
            for group in self.supporting_groups:
                print("-", group)

    def collect_rubbish(self):
        location_name = self.location.name

        if location_name in self.cleaned_locations:
            print("You already collected rubbish here.")
        else:
            self.cleaned_locations.append(location_name)
            print("You collected the rubbish at", location_name)
            print("Take it to the Castle for proper disposal.")

    def collect_evidence(self):
        if self.location.name != "Forest":
            print("Look for pollution evidence in the Forest.")

        elif self.has_evidence:
            print("You have already recorded the evidence.")

        else:
            self.has_evidence = True
            print("You record the rubbish dumped beside the river.")
            print("Show your evidence to villagers at the Cave and Castle.")

    def talk_to_villagers(self):
        location_name = self.location.name

        if location_name == "Forest":
            print("There are no villagers here.")
            return False

        if not self.has_evidence:
            print("The villagers need evidence before agreeing to help.")
            print("Collect evidence in the Forest first.")
            return False

        if location_name in self.supporting_groups:
            print("This group has already agreed to help.")
        else:
            self.supporting_groups.append(location_name)
            print("You explain the pollution problem and show your evidence.")
            print("The villagers at the", location_name, "agree to help.")

        if "Cave" in self.supporting_groups:
            if "Castle" in self.supporting_groups:
                print()
                print("Both groups organise a river restoration project.")
                print("Together, they remove rubbish and repair the filter.")
                print("The village has clean water again!")
                print("YOU WIN!")
                return True

        return False