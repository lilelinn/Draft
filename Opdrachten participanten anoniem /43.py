#schrijf je code hier 

class Card:
    def __init__(self, suit: list[str], value: list[str]) -> None:

        self.suit = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        self.value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Ace', 'Queen', 'King', 'Jack']
        

    def description(n: None) -> str:
        print(f"The card is {Card}")



if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de 'play button' rechtsboven
    
    # test class Card
    card = Card(suit='Spades', value='Ace')
    print(card.description())
    

    
        
        
    