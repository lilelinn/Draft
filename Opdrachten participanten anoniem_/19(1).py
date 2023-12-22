##schrijf je code hier
# Opdracht 1

class Card:
    def __init__(self, suit: str, value: str) -> None:
        """
        Initializes a new instance of the class.

        Args:
            suit (str): The suit of the object.
            value (str): The value of the object.
        """
        self._suit = suit
        self._value = value

    def description(self) -> str:
        """
        Returns a string that represents the description of the entire function, description.

        :return: A string that represents the description of the entire function.
        :rtype: str
        """
        return self._value + " of " + self._suit

class Deck:

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
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
    test = Card("2", "Ace")
    print(test.description())
    test2 = Deck()
    print([card.description() for card in test2._cards])

