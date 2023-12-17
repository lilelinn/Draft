# schrijf hier je code


class Card:
    def __init__(self, suit, value) -> None:
        """
        Initialize a new Card instance.

        Args:
            suit (str): The suit of the card.
            value (str): The value of the card.

        Example:
            >>> card = Card("Spades", "10")
            >>> card.suit
            'Spades'
            >>> card.value
            '10'
        """
        self.suit = suit
        self.value = value
    
    def description(self) -> str:
        """
        Return a description of the entire function, its parameters, and its return types.
        >>> card = Card("10", "Spades")
        >>> card.description()
        'This card is a Spades of 10'
        """

        return f"This card is a {self.value} of {self.suit}"


class Deck:
    def __init__(self) -> None:
        """
        Initialize a new Deck instance.

        Example:
            >>> deck = Deck()
            >>> len(deck._cards)
            52
        """
        self._suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self._values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self._cards = []

        for suit in self._suits:
            for value in self._values:
                self._cards.append(Card(suit, value))

if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de play button rechtsbovenin
    deck = Deck()
    print(len(deck._cards))
    card = Card("10", "Spades")
    print(card.description())