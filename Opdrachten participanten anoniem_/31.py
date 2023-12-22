class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self._suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self._values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self._cards = [Card(suit, value) for suit in self._suits for value in self._values]

    def get_deck(self):
        return self._cards

if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de 'play button' rechtsboven
    deck = Deck()
    print(deck)
    # test class Card
    card = Card(suit='Spades', value='Ace')
    print(card)
    
    # test class Deck
    my_deck = Deck()
    print(f"Deck created with {len(my_deck._cards)} cards")
    for card in my_deck._cards:
        print(f"Card: {card.value} of {card.suit}")