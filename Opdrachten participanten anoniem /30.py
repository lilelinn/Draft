#schrijf je code hier 

class Card:
        def __init__(self, suit: str, value: str) -> None:
            """This function initializes a card with a suit and a value.
            >>> card = Card('Spades', 'Ace')
            >>> card.suit
            'Spades'"""
            self.suit = suit
            self.value = value
            
            pass
        
        def description(self) -> str:
            """Returns a description of the card which is the suit.
            >>> card = Card('Spades', 'Ace')
            >>> card.description()
            'The suit is Spades'"""
            return f"The suit is {self.suit}"

class Deck:
     def __init__(self) -> None:
        """This function initializes the deck with 52 cards.
        >>> deck = Deck()
        >>> len(deck._cards)
        52"""
        self._suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self._values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self._cards = []
        for suit in self._suits:
            for value in self._values:
                self._cards.append(Card(suit, value))
        pass

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