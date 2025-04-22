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
            sys.exit()
        except: 
            print(f"Invalid input, {u}. Try again")
            continue

def _computer_hand() -> str:
    return random.choice((_R, _P, _S))



def _determine_win(u: str, c: str) -> str:
    if c == u:
        return TIE
    if u == _R and c == _S or u == _P and c == _R or u == _S and c == _P:
        return WIN
    return LOSS


def play_a_round() -> str: 
    u = _user_hand()
    c = _computer_hand()
    print(f"You -- {_to_str(u)} vs {_to_str(c)} -- Computer")

    return _determine_win(u, c)


def _to_str(h: str) -> str:
    if h == _R: 
        return "Rock"
    elif h == _P:
        return "Paper"
    elif h == _S:
        return "Scissors"
    else:
        return ""


if __name__ == "__main__":
    play_a_round()
