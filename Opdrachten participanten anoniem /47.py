#schrijf je code hier 

class Card:
    def __init__(self, suit: str, value: str) -> None:
        """
        Initialiseert een nieuwe instantie van de Card-klasse 
        met de gegeven suit en value attributen.

        >>> card = Card('spades', 'A')
        >>> card.suit
        'spades'
        >>> card.value
        'A'
        """

        self.suit = suit
        self.value = value
    
    def description(self) -> str:
        """
        Returns a string containing the card's value and suit.

        >>> card = Card('hearts', 'Q')
        >>> card.description()
        'This card is a Q of hearts'
        """

        return f"This card is a {self.value} of {self.suit}"

class Deck:
    def __init__(self) -> None:
        """
        Initializes a new instance of the Deck class.

        """
        self._suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self._values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
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