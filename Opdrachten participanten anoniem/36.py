#schrijf je code hier 
class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value
        

    def description(self) -> str:
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self, _suits, _values, _cards) -> None:
        self._suits = _suits
        self._values = _values
        self._cards = [(i,j) for i in self._suits for j in self._values]




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