import sys
import random

_R, _P, _S = 'r', 'p', 's'
WIN, LOSS, TIE = 'w', 'l', 't'


def _user_hand() -> str:
    while True: 
        try:
            u = input("Rock (r), Paper (p), or Scissors (s)?").strip()
            return u[0].lower()
        except (EOFError, KeyboardInterrupt):
            print("\nThanks for playing the game!")
