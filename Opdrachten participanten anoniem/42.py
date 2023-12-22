#schrijf je code hier 
class Card:
    def __init__(self, value, suit):
        """
        Initialize a new card with the given suit and value.

        >>> card = Card('Hearts', 'Ace')
        >>> card.suit
        'Hearts'
        >>> card.value
        'Ace'
        """
        self.value = value
        self.suit = suit
    
    def description(self):
        """
        Return a string representing the card's description.

        >>> card = Card('Hearts', 'Ace')
        >>> card.description()
        'Ace of Hearts'
        """
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        """
        Initialize a new deck of cards.

        >>> deck = Deck()
        >>> len(deck._cards)
        0
        >>> deck._suits
        ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        >>> deck._values
        ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        """
        self._suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self._values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self._cards = []
        for suit in self._suits:
            for value in self._values:
                card = Card(suit, value)
                self._cards.append(card)

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
    
        
        
    