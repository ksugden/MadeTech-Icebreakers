from random import randint

with open("data/cards.txt") as file:
    cards = file.read().splitlines()

def random_card():
    return cards[randint(0,len(cards)-1)]

class RandomCard:    
    def __init__(self) -> None:
        self.text = random_card()