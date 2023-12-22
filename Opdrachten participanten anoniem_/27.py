#schrijf je code hier 
class Card:
    """
    >>> card = Card('Spades', 'Ace')
    >>> card.suit
    'Spades'
    >>> card.value
    'Ace'
    >>> card.description()
    'This card is a Ace of Spades'

    Returns:
    str: A description of the card based on its suit and value.
    """
    def __init__(self, suit, value):
        """
        Maakt een nieuwe instantie van de klasse Card.
        Slaat de suit en value op in nieuwe attributen.
        """
        self.suit = suit
        self.value = value
    def description(self):
        """
        Returnt een print statement op basis van de suit en value.
        """
        return f"This card is {self.value} of {self.suit}"

class Deck:
    """
    Deze functie maakt een nieuw deck aan van elke mogelijkheid.
    En returnt een print statement van de lengte van de deck.

    >>> deck = Deck()
    >>> len(deck._cards)
    52
    >>> card = deck._cards[0]
    >>> card.description()
    'Ace of Spades'
    >>> deck.description()
    'Deck created with 52'

    Returns:
    str: A description of the deck created with the length of the cards in the deck.
    """
    def __init__(self):
        """
        Maakt een nieuw deck aan van elke mogelijkheid.
        """
        self._cards = []
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for value in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
                self._cards.append(Card(suit, value))
        
    def description(self):
        """
        Returnt een print statement van de lengte van de deck.
        """
        return f"Deck created with {len(self._cards)}"

if __name__ == "__main__":
    # schrijf je test hier
    """
    >>> deck = Deck()
    >>> len(deck._cards)
    52
    >>> card = deck._cards[0]
    >>> card.description()
    'Ace of Spades'
    >>> deck.description()
    'Deck created with 52'
    """
    # test door middel van de 'play button' rechtsboven
    
    # test class Card
    card = Card(suit='Spades', value='Ace')
    print(card.description())
    
    # test class Deck
    my_deck = Deck()
    print(f"Deck created with {len(my_deck._cards)}")
    for card in my_deck._cards:
        print(f"Card: {card.value} of {card.suit}")