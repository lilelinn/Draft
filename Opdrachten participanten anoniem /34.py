#schrijf je code hier 

class Card:
        def __init__(self, suit:str, value: str):
            self.suit = suit
            self.value = value

        def description(self):
            return f"card is {self.suit} and {self.value}"

class Deck:
        def __init__(self):
            self.suits = ['spades','hearts','clubs','diamons' ]
            self.values = [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K','A']
            z= []
            for x in self.suits:
                for y in self.values:
                    z.append(Card(x,y))
            self.values = z
            



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
    

    