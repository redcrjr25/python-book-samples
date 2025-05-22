from enum import Enum

class Hand(Enum):
    ROCK, PAPER, SCISSORS = "r", "p", "s"

    def __str__(self) -> str:
        match self:
            case Hand.ROCK:
                return "Rock"
            case Hand.PAPER:
                return "Paper"
            case Hand.SCISSORS:
                return "Scissors"
            case _:
                raise ValueError

def compare_hands(h1: Hand, h2: Hand) -> int:
    match (h1, h2):
        case (
            (Hand.ROCK, Hand.SCISSORS)
            | (Hand.PAPER, Hand.ROCK)
            | (Hand.SCISSORS, Hand.PAPER)
        ):
            return 1
        case (
            (Hand.SCISSORS, Hand.ROCK)
            | (Hand.ROCK, Hand.PAPER)
            | (Hand.PAPER, Hand.SCISSORS)
        ):
            return -1
        case _:
            return 0
