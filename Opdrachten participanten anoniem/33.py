#schrijf je code hier 



class Card:
    
    def __init__(self, suit: list[str], value: list[str]) -> None:
        
        """
        >>> python_Card.suit
        ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        >>> python_Card.value
        ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Ace', 'Jack', 'Queen', 'King']
        """


        self.suit = suit
        self.value = value

    def description(self) -> int:

        return(f" {value}, of, {suit}")
    



class Deck:
    def __init__(self, suits: list[str], values: list[str], cards: ) -> None:   
    

        """
        >>> python_Deck.suits
        ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        >>> python_Deck.values
        ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Ace', 'Jack', 'Queen', 'King']
        """
    self.suits = suits
    self.values = values
    self.cards = cards
    
    create empty list of cards
    for each suit do
            for each value do 
                    create new Card with that combination
                    add it to the last
    

    
    
    





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
    
        
        
    