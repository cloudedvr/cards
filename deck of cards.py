import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.populate()

    def populate(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def switch_places(self):
        if len(self.cards) >= 2:
            index1, index2 = random.sample(range(len(self.cards)), 2)
            self.cards[index1], self.cards[index2] = self.cards[index2], self.cards[index1]

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# Example usage:
if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print("Dealing a card:", deck.deal())
    print("Remaining cards:", deck)
    print("Switching places of two cards:")
    deck.switch_places()
    print(deck)
