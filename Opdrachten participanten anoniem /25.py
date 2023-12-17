# Hier komt je code
class str('Card'):
    def __init__(self, suit: str, value: str, /) -> None:
        """
        Definieert de variabelen in de class

        >>> __init__(self, 'Spades', 'Ace')
        None
        """

        self.suit = suit
        self.value = value
    
    def __description__(self, suit:str, value:str, /) -> str:
        """
        Voegt de suit en de value samen tot een enkele string.

        >>> __description__(self, 'Spades', 'Ace')
        'Ace of Spades'
        >>> __description__(self, 'Hearts', 'Jack')
        'Jack of Hearts'
        >>> __description__(self, 'Clubs', '2')
        '2 of Clubs'
        """

        print(f"{value} of {suit}")

class str('Deck'):
    def __init__(self) -> None:
        """
        Initieert een lege list (self._cards) en voegt daaraan iedere mogelijke kaart toe.

        >>> __init__(Deck)
        ['2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades',  '9 of Spades', '10 of Spades', 'Jack of Spades'] 
        """

        self._suit = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        self._values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self._cards = []
        for y in suit:
            for x in values:
                new_card = __description__(y, x)
                self._cards.append(new_card)
        return self._cards


if __name__ == "__main__":
    # hier komen eventuele tests
    pass
    #geen tests te doen (?)