# schrijf je code hier
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def description(self):
        return f"{self.value} of {self.suit}"
    
class Deck:
    def __init__(self):
        self._suits = ["spades", "hearts", "clubs", "diamonds"]
        self._values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
        self._cards = []

        for suit in self._suits:
            for value in self._values:
                card = Card(suit, value)
                self._cards.append(card)

if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de play button rechtsboveninif __name__ == "__main__":
        # Test code here
        card = Card("spades", "ace")
        print(card.description())
    
        deck = Deck()
        for card in deck._cards:
            print(card.description())