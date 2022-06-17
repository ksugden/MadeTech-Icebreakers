from random import randint


with open("cards.txt") as file:
    cards = file.read().splitlines()


def random_card():
    return cards[randint(0,len(cards)-1)]


print(random_card())
