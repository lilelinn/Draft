# schrijf je code hier

class Card:
    def __init__(self, suit, value):
        """
        Initialize a new Card object.

        Args:
            suit (str): The suit of the card.
            value (str): The value of the card.

        Examples:
            >>> card = Card('spades', 'ace')
            >>> card.suit
            'spades'
            >>> card.value
            'ace'
        """
        self.suit = suit
        self.value = value

    def description(self):
        """
        Generate a description of the card.

        >>> card = Card('spades', 'ace')
        >>> card.description()
        'This card is a ace of spades'

        >>> card = Card('hearts', 'queen')
        >>> card.description()
        'This card is a queen of hearts'
        """
        return f"This card is a {self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self._suit = ['spades', 'hearts', 'clubs', 'diamonds']
        self._values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'ace', 'jack', 'queen', 'king']
        self._cards = []

        for suit in self._suit:
            for value in self._values:
                self._cards.append(Card(suit, value))

if __name__ == "__main__":
    card = Card('spades', 'ace')
    assert card.suit == 'spades'
    assert card.value == 'ace'
    
    card = Card('hearts', 'queen')
    assert card.description() == 'This card is a queen of hearts'