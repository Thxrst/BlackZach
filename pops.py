import random


class Game:
    def __init__(self):
        self.players = []
        self.number_of_decks = 1
        self.dealer = Player("Dealer", is_dealer=True)

        self.deck = None

    def deal(self):
        """
        give one card to each player
        give one card to the dealer

        :return:
        """
        for player in self.players:
            self.deck.hit(player)

        self.deck.hit(self.dealer)

    def play(self):
        print("Welcome to Pop's BlackZach")
        print("")

        print("Let's setup the players")
        print("")
        while True:
            x = input("Enter player Name - Q and Enter when done:\n")
            if x and x.strip() != "":
                if x.strip().lower() == "q":
                    break

                if x not in [x.name for x in self.players]:
                    self.players.append(Player(name=x))
            else:
                print("You must enter a player name")

        print("The players for the game are:")
        for x in self.players:
            print(x.name)

        while True:
            x = input("How many decks would you like to play with (defaults to 1)")
            if x.isdigit():
                self.number_of_decks = int(x)
                break
            else:
                print(
                    "You need to enter a number for the number of decks to be in play."
                )

        print(f"We will be playing with {self.number_of_decks} decks of cards.")

        print("Let's shuffle the cards")

        self.deck = Deck(number_of_decks=self.number_of_decks)
        self.deck.shuffle()

        print("Now we'll deal the cards...")
        self.deal()

        self.show_hands()

        for player in self.players:
            player.play(self.deck)

        self.dealer.play()

        return

    def show_hands(self):
        for player in self.players:
            player.show_hand()

        self.dealer.show_hand()


class Player:
    def __init__(self, name, is_dealer=False):
        self.name = name
        self.is_dealer = is_dealer

        self.hand = Hand()

        self.possible_totals = []

    def show_hand(self):
        if self.is_dealer:
            #  don't show the first card
            print(
                f"{self.name} has %s - showing: %s"
                % (
                    ", ".join(self.hand.cards[1:]),
                    ", ".join(str(x) for x in self.possible_totals),
                )
            )
        else:
            print(
                f"{self.name} has %s - totaling: %s"
                % (
                    ", ".join(self.hand.cards),
                    ", ".join(str(x) for x in self.possible_totals),
                ),
            )

    def hit(self, card):
        self.hand.add(card)

        total = 0
        soft_total = 0
        for i, card in enumerate(self.hand.cards):
            if self.is_dealer and i == 0:
                continue
            value = Card.get_value(card)
            if isinstance(value, list):
                soft_total += value[1:]
                total += value[0:1]
            else:
                soft_total += value
                total += value

        self.possible_totals = []
        self.possible_totals.append(total)
        if total != soft_total:
            self.possible_totals.append(soft_total)

    def play(self, deck):
        while True:
            self.show_hand()
            x = input("(H)it or (S)tay?")
            if x.lower() == "h":
                deck.hit(self)
            else:
                return


class Deck:
    def __init__(self, number_of_decks=1):
        single_deck = [
            "AC",
            "KC",
            "QC",
            "JC",
            "10C",
            "9C",
            "8C",
            "7C",
            "6C",
            "5C",
            "4C",
            "3C",
            "2C",
            "AS",
            "KS",
            "QS",
            "JS",
            "10S",
            "9S",
            "8S",
            "7S",
            "6S",
            "5S",
            "4S",
            "3S",
            "2S",
            "AH",
            "KH",
            "QH",
            "JH",
            "10H",
            "9H",
            "8H",
            "7H",
            "6H",
            "5H",
            "4H",
            "3H",
            "2H",
            "AD",
            "KD",
            "QD",
            "JD",
            "10D",
            "9D",
            "8D",
            "7D",
            "6D",
            "5D",
            "4D",
            "3D",
            "2D",
        ]

        self.deck = []
        for i in range(0, number_of_decks):
            self.deck.extend(single_deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def hit(self, player):
        card = self.deck[0]
        player.hit(card)
        self.deck.pop(0)


class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)


class Card:
    @staticmethod
    def get_value(card):
        card_without_suit = (
            card.replace("C", "").replace("S", "").replace("H", "").replace("D", "")
        )

        if card_without_suit in ("K", "Q", "J"):
            return 10
        elif card_without_suit == "A":
            return [1, 11]
        else:
            return int(card_without_suit)


if __name__ == "__main__":
    g = Game()
    g.play()
