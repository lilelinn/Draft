#schrijf je code hier 
# 1

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def description(self):
        """
        Geeft de beschrijving van de kaart.
        >>> description("Ace", "Spade")
        Ace of Spade
        """
        print(f"{self.value} of {self.suit}")

class Deck:
    def __init__(self):
        self._suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self._values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        self._cards = []

        for x in self._suits:
            for y in self._values:
                return card.append(self._cards)

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
    
        
  