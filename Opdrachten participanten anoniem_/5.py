#schrijf je code hier 
class Card:
    def __init__(self, suit, value):
        """
        Initializes a new instance of the class.

        Parameters:
            suit (str): The suit of the card.
            value (int): The value of the card.

        Returns:
            None
        """
        self.suit = suit
        self.value = value
    
    def description(self):
        """
        Return a description of the entire function, its parameters, and its return types.
        """
        return f"{self.value} of {self.suit}"
    
class Deck:
    def __init__(self):
        """
        Initializes a new instance of the Deck class.

        Parameters:
            self (Deck): The Deck instance.

        Returns:
            None
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