print("Starting the rock, paper, scissors game...")
from rock_paper_scissors import user_hand, computer_hand, determine_win, WIN
from output import print_result

def f2(max_rounds: int = 3) -> None:
    """Plays a fixed number of rounds and prints total wins and rounds."""
    print(f"Playing {max_rounds} rounds...")
    wins = 0
    for i in range(max_rounds):
        print(f"Starting round {i+1}...")
        user = user_hand()
        print(f"User chose: {user}")
        computer = computer_hand()
        print(f"Computer chose: {computer}")
        result = determine_win(user, computer)
        print_result(user, computer, result)
        if result == WIN:
            wins += 1
    print(f"You won {wins} out of {max_rounds} rounds.")

    if __name__ == "__main__":
        print("Entering main block...")
        f2(3)

    