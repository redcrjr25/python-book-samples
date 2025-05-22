from typing import Optional
from rps.hand import Hand

def read_hand() -> Optional[Hand]:
    while True:
        try:
            i = input("Rock (r), Paper (p), or Scissors (s)?").lower()
            if i.startswith("q") or i.startswith("x"):
                return

            return _parse_hand(i[0])
        except (EOFError, KeyboardInterrupt):
            return
        except:
            print("Invalid input. Try again.")
            continue

def _parse_hand(s: str) -> Hand:
    match s:
        case "r":
            return Hand.ROCK
        case "p":
            return Hand.PAPER
        case "s":
            return Hand.SCISSORS
        case _:
            raise ValueError("Invalid hand")
