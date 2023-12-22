#schrijf je code hier
#opdracht 1
class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def description(self) -> str:
        """
        Return a description of the card.
        >>> card = Card("Hearts", "Ace")
        >>> card.description()
        'De kaart is Ace of Hearts.'
        >>> card2 = Card("Spades", "7")
        >>> card2.description()
        'De kaart is 7 of Spades.'
        """
        return f"De kaart is {self.value} of {self.suit}."

#opdracht 2
class Deck:
    def __init__(self) -> None:
        self._suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self._values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "Jack", "Queen", "King"]
        self._cards = []

        # Kaartendeck genereren
        for suit in self._suits:
            for value in self._values:
                self._cards.append(Card(suit, value))





if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de 'play button' rechtsboven 

    # zelf toegevoegd door Floor
    card1 = Card(suit='Spades', value='Ace')
    card2 = Card(suit='Hearts', value='King')
    print(card1.description())
    print(card2.description())
    
    # Create an instance of the Deck class
    my_deck = Deck()

    # Print some information to check if the deck is created correctly
    print("Deck created with {} cards.".format(len(my_deck._cards)))

    # You can also loop through the cards and print their values to verify
    for card in my_deck._cards:
        print("Card: {} of {}".format(card.value, card.suit))