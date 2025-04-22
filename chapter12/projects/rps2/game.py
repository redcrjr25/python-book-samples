from typing import Final
from output import *
from rock_paper_scissors import play_a_round, WIN, LOSS

MAX_ROUNDS: Final[int] = 3


def play(max_rounds: int = MAX_ROUNDS):
    """Play max_rounds of Rock Paper Scissors."""

    start_banner()

    wins: int = 0
    for _ in range(max_rounds):
        wlt = play_a_round()
        print_result(wlt)
        wins += 1 if wlt == WIN else 0
        horz_bar()

    end_banner(wins, max_rounds)


def print_result(wlt: str):
    """Print a text corresponding to win/loss/tie."""

    if wlt == WIN:
        print("You win!")
    elif wlt == LOSS:
        print("You lose!")
    else:
        print("Tie!")


if __name__ == "__main__":
    play()
