import random

#schrijf je code hier 
Class Card:
""" Een Class genaamd Card met twee functies. De attributen zijn 
de kleur en waarde van een kaart.
"""

    def __init__(self, suit: str, value: str) -> None:

    def description(self) -> str:
    """ geeft de kleur van een kaart en de waarde
    """

    kleur = [random.choice[('Spades', 'Hearts', 'Clubs', 'Diamonds')] for x in range(1)]
    waarde = [random.choice[('2', '3', 'Ace', 'Jack')] for x in range(1)]

    print(kleur, waarde)

Class Deck:

""" bevat alleen een initilizer functie"""
    def __init__(self) -> None:
    """ bevat een lijst met suits, values en kaartendek
    """

    self.suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    self._values = ['2', '3', 'Ace', 'Jack']
    
    self._cards = []

    for x in suit:
        for x in value:

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