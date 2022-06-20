from random import choice


with open("data/cards.txt") as file:
    cards = file.readlines()


def random_card():
    return choice(cards)


class RandomCard:    
    def __init__(self) -> None:
        self.text = random_card()