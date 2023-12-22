#schrijf je code hier
class Card:
    "card"
    def __init__(self, suit:str, value: str) -> None:
        """ create a new card
        >>> python_card = Card(\
        'Hearts'\
        'Ace'
        )
        >>> python_card.suit
        'Hearts'
        >>> python_card.value
        'Ace'
        """
        self.suit = suit
        self.value = value
    def description(self) -> str:
        """
        """
        return f"de kaart is {self.suit}{self.value}"








if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de 'play button' rechtsboven 
    python_card = Card(\
        'Hearts'\
        'Ace'
        )
    print(python_card)