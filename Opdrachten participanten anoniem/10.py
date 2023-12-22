# hier komt je code
import random
import doctest
def definition (suit:str, value:str):
    suit_options = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    suit = random.shuffle(suit_options)[0]
    value_options = ['2','3','Ace', 'Jack']
    value = random.shuffle(value_options)[0]
    print(value)
    return value

if __name__ == "__main__":
    # hier komen je test
    print("klopt")
else:
    print("klopt")
