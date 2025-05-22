# Lab 15.3 Playing Cards printing all 52 cards from the deck

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        ranks = [
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        ]
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None  # Or raise an exception if preferred

    def __str__(self):
        deck_str = ""
        for card in self.cards:
            deck_str += str(card) + "\n"
        return deck_str

# Example usage
deck = Deck()
print("Initial Deck:")
print(deck)

deck.shuffle()
print("\nShuffled Deck:")
print(deck)

print("\nDealing a few cards:")
for _ in range(5):
    card = deck.deal()
    if card:
        print(card)
    else:
        print("No more cards in the deck")
