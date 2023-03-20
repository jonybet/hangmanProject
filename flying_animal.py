import random

words = [
    "Eagle",
    "Mockingjay",
    "Seagull",
    "Butterfly",
    "Dragonfly",
    "Bee",
    "Bats",
    "Willow",
    "Parrot",
    "Goose"
]

def get_random_word():
    flying_animals = random.choice(words)
    return flying_animals
