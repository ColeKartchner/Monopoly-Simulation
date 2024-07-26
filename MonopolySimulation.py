import random
from collections import defaultdict

class MonopolySimulation:
    def __init__(self):
        # Initialize the board, player position, number of moves, and jail-free cards
        self.board = [0] * 40  # 40 spaces on the board
        self.position = 0
        self.moves = 0
        self.jail_free_cards = 0
        self.chance_deck = self.create_chance_deck()
        self.community_chest_deck = self.create_community_chest_deck()
        self.jail_free_chance = False
        self.jail_free_community = False
        self.in_jail = False
        self.jail_turns = 0

    def create_chance_deck(self):
        # Create and shuffle the Chance deck
        deck = [
            "Advance to Go", "Advance to Boardwalk", "Advance to Illinois Avenue",
            "Advance to St. Charles Place", "Advance to nearest Railroad",
            "Advance to nearest Railroad", "Advance token to nearest Utility",
            "Bank pays you dividend of $50", "Get Out of Jail Free",
            "Go Back 3 Spaces", "Go to Jail", "Make general repairs on all your property",
            "Speeding fine $15", "Take a trip to Reading Railroad",
            "You have been elected Chairman of the Board", "Your building loan matures"
        ]
        random.shuffle(deck)
        return deck

    def create_community_chest_deck(self):
        # Create and shuffle the Community Chest deck
        deck = [
            "Advance to Go", "Bank error in your favor", "Doctor’s fee",
            "From sale of stock you get $50", "Get Out of Jail Free", "Go to Jail",
            "Holiday fund matures", "Income tax refund", "It is your birthday",
            "Life insurance matures", "Pay hospital fees of $100", "Pay school fees of $50",
            "Receive $25 consultancy fee", "You are assessed for street repair",
            "You have won second prize in a beauty contest", "You inherit $100"
        ]
        random.shuffle(deck)
        return deck

    def roll_dice(self):
        # Simulate rolling two six-sided dice
        return random.randint(1, 6), random.randint(1, 6)

    def move_player(self, dice_roll):
        # Update player's position and handle special spaces
        self.position = (self.position + sum(dice_roll)) % 40
        self.board[self.position] += 1
        self.moves += 1
        # Handle special spaces
        if self.position == 30:  # Go to Jail
            self.go_to_jail()
        elif self.position in [7, 22, 36]:  # Chance
            self.draw_chance_card()
        elif self.position in [2, 17, 33]:  # Community Chest
            self.draw_community_chest_card()

    def go_to_jail(self):
        # Send player to jail
        self.position = 10
        self.in_jail = True
        self.jail_turns = 0

    def draw_chance_card(self):
        # Draw and process a Chance card
        card = self.chance_deck.pop(0)
        self.chance_deck.append(card)  # Put the card at the end of the deck
        if card == "Advance to Go":
            self.position = 0
        elif card == "Advance to Boardwalk":
            self.position = 39
        elif card == "Advance to Illinois Avenue":
            self.position = 24
        elif card == "Advance to St. Charles Place":
            self.position = 11
        elif card == "Advance to nearest Railroad":
            if self.position == 7:
                self.position = 15
            elif self.position == 22:
                self.position = 25
            elif self.position == 36:
                self.position = 5
        elif card == "Advance token to nearest Utility":
            if self.position == 7 or self.position == 36:
                self.position = 12
            elif self.position == 22:
                self.position = 28
        elif card == "Bank pays you dividend of $50":
            pass  # No action needed for simulation
        elif card == "Get Out of Jail Free":
            self.jail_free_chance = True
        elif card == "Go Back 3 Spaces":
            self.position -= 3
        elif card == "Go to Jail":
            self.go_to_jail()
        elif card == "Make general repairs on all your property":
            pass  # No action needed for simulation
        elif card == "Speeding fine $15":
            pass  # No action needed for simulation
        elif card == "Take a trip to Reading Railroad":
            self.position = 5
        elif card == "You have been elected Chairman of the Board":
            pass  # No action needed for simulation
        elif card == "Your building loan matures":
            pass  # No action needed for simulation

    def draw_community_chest_card(self):
        # Draw and process a Community Chest card
        card = self.community_chest_deck.pop(0)
        self.community_chest_deck.append(card)  # Put the card at the end of the deck
        if card == "Advance to Go":
            self.position = 0
        elif card == "Bank error in your favor":
            pass  # No action needed for simulation
        elif card == "Doctor’s fee":
            pass  # No action needed for simulation
        elif card == "From sale of stock you get $50":
            pass  # No action needed for simulation
        elif card == "Get Out of Jail Free":
            self.jail_free_community = True
        elif card == "Go to Jail":
            self.go_to_jail()
        elif card == "Holiday fund matures":
            pass  # No action needed for simulation
        elif card == "Income tax refund":
            pass  # No action needed for simulation
        elif card == "It is your birthday":
            pass  # No action needed for simulation
        elif card == "Life insurance matures":
            pass  # No action needed for simulation
        elif card == "Pay hospital fees of $100":
            pass  # No action needed for simulation
        elif card == "Pay school fees of $50":
            pass  # No action needed for simulation
        elif card == "Receive $25 consultancy fee":
            pass  # No action needed for simulation
        elif card == "You are assessed for street repair":
            pass  # No action needed for simulation
        elif card == "You have won second prize in a beauty contest":
            pass  # No action needed for simulation
        elif card == "You inherit $100":
            pass  # No action needed for simulation

    def simulate_game(self, turns, strategy):
        # Run the simulation for a specified number of turns using the chosen strategy
        for _ in range(turns):
            if self.in_jail:
                self.handle_jail(strategy)
            else:
                dice_roll = self.roll_dice()
                self.move_player(dice_roll)

    def handle_jail(self, strategy):
        # Handle the player's time in jail based on the specified strategy
        if strategy == 'A':
            if self.jail_free_chance or self.jail_free_community:
                self.in_jail = False
                if self.jail_free_chance:
                    self.jail_free_chance = False
                elif self.jail_free_community:
                    self.jail_free_community = False
            else:
                self.in_jail = False
        elif strategy == 'B':
            if self.jail_free_chance or self.jail_free_community:
                self.in_jail = False
                if self.jail_free_chance:
                    self.jail_free_chance = False
                elif self.jail_free_community:
                    self.jail_free_community = False
            elif self.jail_turns < 3:
                dice_roll = self.roll_dice()
                if dice_roll[0] == dice_roll[1]:
                    self.in_jail = False
                else:
                    self.jail_turns += 1
            else:
                self.in_jail = False

    def print_results(self):
        # Print the results of the simulation
        for i, count in enumerate(self.board):
            print(f"Space {i}: {count} landings ({(count / self.moves) * 100:.2f}%)")

# Simulation parameters
turns_list = [1000, 10000, 100000, 1000000]
strategies = ['A', 'B']

for strategy in strategies:
    print(f"Strategy {strategy}:")
    for turns in turns_list:
        print(f"Running simulation for {turns} turns...")
        simulation = MonopolySimulation()
        simulation.simulate_game(turns, strategy)
        simulation.print_results()
        print("\n")
