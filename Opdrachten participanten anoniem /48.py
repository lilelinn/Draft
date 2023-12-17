class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
        
    def description(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self._suit = ['Spades','Hearts','Clubs','Diamonds']
        self._value = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        self._cards = [Card(self._value, self._suit) for suit in self._suit]

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
    
        
        
    