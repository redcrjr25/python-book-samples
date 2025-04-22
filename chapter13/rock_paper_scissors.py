import random

WIN = "win"
LOSE = "lose"
TIE = "tie"


def user_hand():
    return input("Rock (r), Paper (p), or Scissors (s)? ").strip().lower()


def computer_hand():
    return random.choice(["r", "p", "s"])


def determine_win(user, computer):
    if user == computer:
        return TIE
    if (
        (user == "r" and computer == "s")
        or (user == "p" and computer == "r")
        or (user == "s" and computer == "p")
    ):
        return WIN
    return LOSE
