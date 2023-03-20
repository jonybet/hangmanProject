import random

words = [
    "Lion",
    "Wolf",
    "Cougar",
    "Cheetah",
    "Tiger",
    "Zebra",
    "Deer",
    "Bear",
    "Kangaroo",
    "Giraffe"
]

def get_random_word():
    land_animals = random.choice(words)
    return land_animals
