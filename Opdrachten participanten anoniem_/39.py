#schrijf je code hier 





if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de 'play button' rechtsboven
    
    # test class Card
    card = Card(suit='Spades', value='Ace')
    print(card.description())
    
class Card:

    def __init__(self, suit: str, value: str) -> None:
        self._suit = suit
        self._value = value

    def description(self) -> str:
       return self.value + " of " + self.suit
        

    # test class Deck
    my_deck = Deck()
    print(f"Deck created with {len(my_deck._cards)}")
    for card in my_deck._cards:
        print(f"Card: {card.value} of {card.suit}")
    
        
        
    