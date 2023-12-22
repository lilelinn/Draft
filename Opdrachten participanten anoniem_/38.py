#schrijf je code hier 
import random
class Card:
    def __init__(self, suit, value):
        """
        Initialize a Card object.

        Args:
            suit (str): The suit of the card.
            value (str): The value of the card.

        >>> card = Card("Spades", "Ace")
        >>> card.suit
        'Spades'
        >>> card.value
        'Ace'
        """
        self.suit = suit
        self.value = value
    
    def description(self):
        """
        Get the description of the card.

        >>> card = Card("Hearts", "Queen")
        >>> card.description()
        'This is a Queen of Hearts'
        """
        return f"This is a {self.value} of {self.suit}"

class Deck:
    def __init__(self):
        """
        Initialize a Deck object.
        """
        self._suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self._values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self._cards = self._generate_deck()
    
    def _generate_deck(self):
        """
        Generate a deck of cards.

        Returns:
            list: A list of Card objects representing a deck of cards.
        """
        deck = []
        for suit in self._suits:
            for value in self._values:
                deck.append(Card(suit, value))
        random.shuffle(deck)
        return deck



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
    
        
        
    