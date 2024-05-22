class Player:
    def __init__(self, name):
        self.name = name
        self.location = "forest"
        self.inventory = []
        self.status = "healthy"

    def move(self, destination):
        self.location = destination

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
def forest_challenge(player):
    print("You find a mysterious box in the forest.")
    print("Do you want to open it? (yes/no)")
    choice = input("> ").lower()
    if choice == "yes":
        if "key" not in player.inventory:
            print("The box contains a key You add it to your inventory.")
            player.add_to_inventory("key")
        else:
            print("The box is already opened. Nothing new here.")
    else:
        print("You decide not to open the box. Nothing happens.")

def cave_challenge(player):
    # Example of a different challenge
    print("You enter a dark cave and find a treasure chest!")
    print("Do you want to open it? (yes/no)")
    choice = input("> ").lower()
    if choice == "yes":
        if "treasure" not in player.inventory:
            print("The chest contains treasure You add it to your inventory.")
            player.add_to_inventory("treasure")
        else:
            print("The chest is already opened. Nothing new here.")
    else:
        print("You decide not to open the chest. Nothing happens.")

        def main():
            player_name = input("Enter your character name: ")
    player = Player(player_name)

    while True:
        print(f"\nYou are in {player.location}.")
        if player.location == "forest":
            forest_challenge(player)
        elif player.location == "cave":
            cave_challenge(player)
        # Add more elif conditions for other locations

        # Example of moving to a new location
        print("\nWhere do you want to go next?")
        print("1. Forest")
        print("2. Cave")
        # Add more options for other locations
        choice = input("> ")
        if choice == "1":
            player.move("forest")
        elif choice == "2":
            player.move("cave")
        # Add more elif conditions for other locations

        # Example of checking player's inventory
        print(f"\nYour inventory: {', '.join(player.inventory)}")

        # Example of checking player's status
        print(f"\nYour status: {player.status}")

        # Example of adding a decision that changes the player's status
        if "treasure" in player.inventory:
            print("\nYou feel stronger after finding the treasure.")
            player.status = "stronger"

       

        # Example of ending the game
        if player.status == "win":
            print("\nCongratulations You have won the game!")
            break
        elif player.status == "lose":
            print("\nGame Over!")
            break

if __name__ == "__main__":
    main()

    