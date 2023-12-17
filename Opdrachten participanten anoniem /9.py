#schrijf je code hier
class Card:
    def __init__(self, value: str, suit:str):
        '''
        Zet functies voor het opbouwen van een kaart.
        >>> card1 = Card('A', 'Spades')
        >>> card1.value
        'A'
        >>> card1.suit
        'Spades'
        '''
        self.value = value
        self.suit = suit
    
    def description(self, value, suit):
        '''
        Returns the description of the card

        >>> obj = Card()
        >>> obj.description('Ace', 'Spades')
        'Ace of Spades'
        '''
        return (value + ' of ' + suit)

class Deck:
    def __init__(self):
        '''
        De kaarten in een deck
        
        >>> deck = Deck()
        >>> len(deck)
        52
        '''
        self._suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self._values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self._cards = []
        for x in self._suits:
            for y in self._values:
                card = Card(y,x)
                self._cards.append(card.description(y, x))
        
        print(self._cards)

if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de 'play button' rechtsboven
    classa = Card('Ace', 'Spades')
    classa.description('Ace', 'Spades')
    classb = Deck()