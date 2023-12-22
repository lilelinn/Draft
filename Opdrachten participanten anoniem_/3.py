# schrijf je code hier
class Card:
    """
        Initializes a new instance of the class.
        
        Args:
            suit (str): The suit of the card.
            value (int): The value of the card.
        """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def description(self):
        """
        Returns a description of the card.
        
        >>> card = Card('spades', 'ace')
        >>> card.description()
        'This card is a ace of spades.'
        """
        return f"This card is a {self.value} of {self.suit}."

class Deck:
    """
    Initializes a new instance of the class.

    Args:
        None
    """
    def __init__(self):
        self._suits = ['spades', 'hearts', 'clubs', 'diamonds']
        self._values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'ace', 'jack', 'king', 'queen']
        self._cards = []

        for suit in self._suits:
            for value in self._values:
                self._cards.append(Card(suit, value))

if __name__ == "__main__":
    card = Card('spades', 'ace')
    deck = Deck()

    print(card.description)
    print(deck._cards)
    
#     # schrijf je test hier
#     # test door middel van de play button rechtsbovenin