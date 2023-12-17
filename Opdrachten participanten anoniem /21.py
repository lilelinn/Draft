#schrijf je code hier
class Card:
    Listsuit = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    Listvalue = ['2', '3', '4', '5', '6', '7', '8','9', '10', 'Jack', 'Queen', 'King', 'Ace']
    def __init__(self, suit: Listsuit, value: Listvalue) -> None:
        self.value = value[:]
        self.suit = suit[:]
        pass

    def description(value, suit):
        return value + "of" + suit
        

class Deck:
    def __init__(self, suits: listsuits, values: listvalues, cards: listcards[str]) -> None:
        self.suits = suits
        self.values = values
        self.cards = cards
        pass
    
    def self._cards():
        return
if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de 'play button' rechtsboven

