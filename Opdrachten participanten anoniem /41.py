#schrijf je code hier 
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def description(self):
        return f"{self.value} of {self.suit}"

import random

class Deck:
    def __init__(self):
        self._suits = ["spades", "hearts", "clubs", "diamonds"]
        self._values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
        self._cards = []

        for suit in self._suits:
            for value in self._values:
                card = Card(suit, value)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)


if __name__ == "__main__":
    # schrijf je test hier

    # test door middel van de 'play button' rechtsboven
    
    # test class Card
    card = Card(suit='Spades', value='Ace')
    print(card.description())
    
    # test class Deck
    my_deck = Deck()
    print(f"Deck created with {len(my_deck._cards)}")
    for card in my_deck._cards:
        print(f"Card: {card.value} of {card.suit}")