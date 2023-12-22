#schrijf je code hier 

class Card:
    def __init__(self, rank, suit):
        if isinstance(rank, int):
            if rank < 1 or rank > 10:
                raise ValueError("Invalid rank value for a numeric card.")
        elif rank not in ["Jack", "Ace", "Queen", "King"]:
            raise ValueError("Invalid rank value for a non-numeric card.")
        self.rank = rank
        self.suit = suit

    def description(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self._cards = []
        for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            for rank in ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]:
                self._cards.append(Card(rank, suit))

if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de 'play button' rechtsboven
    
    # test class Card
    card = Card(suit='Spades', rank='Ace')
    print(card.description())
    
    # test class Deck
    my_deck = Deck()
    print(f"Deck created with {len(my_deck._cards)}")
    for card in my_deck._cards:
        print(f"Card: {card.rank} of {card.suit}")
    
        
        
    