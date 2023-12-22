# schrijf je code hier
class Card:
    def __init__(self, color, value):
        """
        Initializes an instance of the class with the given color and value.

        Args:
            color (str): The color of the instance.
            value (int): The value of the instance.

        Returns:
            None
        """
        self.color = color
        self.value = value
    
    def description(self):
        return f"This card is {self.color} {self.value}"


class Deck:
    def __init__(self):
        """
        Initializes a new instance of the class.

        Parameters:
            None

        Returns:
            None
        """
        self._suits = ['spades', 'hearts', 'clubs', 'diamonds']
        self._values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'ace', 'jack', 'king', 'queen']  # Add all the other values as needed
        self._cards = self.generate_card_deck()
    
    def generate_card_deck(self):
        cards = []
        for suit in self._suits:
            for value in self._values:
                card = Card(suit, value)
                cards.append(card)
        return cards

# Example usage
deck = Deck()
for card in deck._cards:
    print(card.description())



if __name__ == "__main__":
    def test_card_description():
        card = Card('spades', 'ace')
        actual_description = card.description()
        expected_description = "This card is spades ace"
        assert actual_description == expected_description, f"Expected: {expected_description}, Actual: {actual_description}"
    
    def test_deck_card_generation():
        deck = Deck()
        actual_length = len(deck._cards)
        expected_length = 16
        assert actual_length == expected_length, f"Expected: {expected_length}, Actual: {actual_length}"
    
        # Check if each card in the deck has a valid description
        for card in deck._cards:
            actual_description = card.description()
            assert isinstance(actual_description, str), f"Expected: str, Actual: {type(actual_description)}"

#     # schrijf je test hier
#     # test door middel van de play button rechtsbovenin