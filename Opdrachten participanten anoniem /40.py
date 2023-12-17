#schrijf je code hier 

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def description(self):
        """
        Returns a formatted string representing the rank and suit of the card.

        Parameters:
            self (Card): The Card object.

        Returns:
            str: A string representing the rank and suit of the card.
        """
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self._cards = []
        for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            for value in ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]:
                self._cards.append(Card(suit, value))
        self._suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self._values = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]




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
    
    