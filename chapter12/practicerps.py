import random

# Constants
R, P, S = "r", "p", "s"
WIN, LOSS, TIE = "w", "l", "t"
MAX_ROUNDS = 5

def user_hand() -> str:
    choice = input("Rock (r), Paper (p), or Scissors (s), or Quit (q)? ").strip()
    if choice.lower() == 'q':
        print("Thanks for playing!")
        exit()
    return choice[0].lower()

def computer_hand() -> str:
    return random.choice([R, P, S])

def determine_win(u: str, c: str) -> str:
    if c == u:
        return TIE
    if u == R and c == S or u == P and c == R or u == S and c == P:
        return WIN
    return LOSS

def to_str(h: str) -> str:
    if h == R:
        return "Rock"
    elif h == P:
        return "Paper"
    elif h == S:
        return "Scissors"
    return ""

def print_result(wlt: str) -> None:
    if wlt == WIN:
        print("You win!")
    elif wlt == LOSS:
        print("You lose!")
    else:
        print("Tie!")

def play() -> None:
    print("Let's play!")
    wins = 0
    for _ in range(MAX_ROUNDS):
        u = user_hand()
        c = computer_hand()
        print(f"You -- {to_str(u)} vs {to_str(c)} -- Computer")
        wlt = determine_win(u, c)
        print_result(wlt)
        if wlt == WIN:
            wins += 1
        print("...")
    print(f"You won {wins} out of {MAX_ROUNDS} rounds.")

if __name__ == "__main__":
    play()