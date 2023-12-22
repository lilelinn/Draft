class Card:
    def __init__(self -> str, suit -> int, value -> int):
        """
        Initializes a new instance of the class with the specified suit and value.

        Parameters:
            suit (str): The suit of the card.
            value (int): The numerical value of the card.

        Returns:
            None
        """
        self.suit = suit
        self.value = value
   
    def description(self -> str):
        """
        Returns a string representing the description of the card.

        Parameters:
            self (Card): The instance of the Card class.

        Returns:
            str: A string representing the description of the card.
        """
        return f"de kaart is {self.suit} {self.value}"
    

class Deck:
    def __init__(self):
        """
        Initializes a new instance of the Deck class.

        Parameters:
            self (Deck): The instance of the Deck class.

        Returns:
            None
        """
        self.suits = ["spades", "hearts", "clubs", "diamonds"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
        self.cards = []

        for suit in self.suits:
            for value in self.values:
                card = Card(suit, value)
                self.cards.append(card)

if __name__ == "__main__"
    my_deck = Deck()
    print("Het kaartendeck bevat", len(my_deck.cards), "kaarten.")