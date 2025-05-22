import random
from rps.hand import Hand

def random_hand() -> Hand:
    return random.choice((Hand.ROCK, Hand.PAPER, Hand.SCISSORS))
