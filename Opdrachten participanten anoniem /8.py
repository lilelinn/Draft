# schrijf je code hier



if __name__ == "__main__":
    # schrijf hier je test
    class card:

        def __init__(self) -> None:
            """
             
            >>> __init__(self)

            """

            self.card = ["spades","hearts","clubs","diamonds"]
            self.value= ["Ace",2,3,4,5,6,7,8,9,10,"joker","queen","king"]

        def description(self, card, value) -> None:

            return f'Je hebt een {card} van {value}'
        
    class deck:

        def __init__(self) -> None:
            """


            >>> __init__(self)

            """

            self._suits = ["spades","hearts","clubs","diamonds"]
            self._values = ["Ace",2,3,4,5,6,7,8,9,10,"joker","queen","king"]
            self._cards = []
            for x in self._suits:
                for y in self._values:
                    self._cards.append((x,y))
