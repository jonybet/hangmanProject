import random

words = [
    "Shark",
    "Whale",
    "Dolphin",
    "Seal",
    "Otter",
    "Killerwhale",
    "Stingray",
    "Lobster",
    "Starfish",
    "Squid"
]

def get_random_word():
    water_animals = random.choice(words)
    return water_animals
