# schrijf je code hier
from typing import List, Any
class Card:
    def __init__(self, suit: str, value: str) -> None:
        """Maakt een kaart met een suit en een value

        >>> my_card = Card( \
            'Spades' \
            '8')
        >>> my_card.suit
        'Spades'
        >>> my_card.value
        '8'
        """
        self.suit = suit
        self.value = value

    def description
    """
    """

class Deck:
    def __init__(self) -> list[str]:
        """
        >>> self._suits[1]
        Hearts
        >>> self._values[5]
        6
        >>> self._cards[0]
        Spades, 1
        """
        self._suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        self._values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
                        'Jack', 'Queen', 'King', 'Ace']
        self._cards = []
        for suit in suits:
            for value in values:
                card = suit + ', ' + value
                self._cards.append(card)
        return self._cards


if _name_ == "_main_":
# schrijf je test hier

