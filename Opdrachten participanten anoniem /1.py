#schrijf je code hier 
cards = Card('2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace')
class Card:
        def __init__(self, suit: str, value: str) -> None:

            """ 
            >>> 
            Card.suit 
            '2'
            """
            self.suit = suit
            self.value = value


        def description(self) -> str;
            """
            >>> 
            
            """
            return f"self.suit and self.value"


class Deck:
     def __init__(self):
          
          self._suits = list['suit''suits''suits''suits']
          self._values = list[value]
          self._cards = list[cards]



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
    
        
        
    