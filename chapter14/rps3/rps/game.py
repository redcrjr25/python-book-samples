# This is the final rock paper scissors game!

import typing
import rps.reader as reader
import rps.rand as rand
from rps.hand import compare_hands
from rps.result import WinOrLose

MAX_ROUNDS: typing.Final[int] = 5

class Game:
    """Game encapsulates the rock paper scissors game functionalities.

    The "main function", start(), plays 5 rounds by default.
    """

    def __init__(self, num_rounds: int = MAX_ROUNDS):
        self._wins = 0
        self._losses = 0
        self._ties = 0
        self._num_rounds = num_rounds

    def start(self):
        """The "main" function. It starts the game."""
        self._banner()
        self._loop()
        self._end_game()

    def _banner(self):
        print(
            """\
---------------------------------
Welcome to Rock Paper Scissors!
Type X or Q to end the game.
---------------------------------\
"""
        )

    def _end_round(self):
        print(
            f"""\
Your wins: {self._wins}, losses: {self._losses}\
out of {self._wins + self._losses + self._ties} rounds
---------------------------------\
"""
        )

    def _end_game(self):
        print(
            f"""\
Thanks for playing Rock, Paper, Scissors!!
Your final score:
Wins: {self._wins}, Losses: {self._losses},\
Total rounds: {self._wins + self._losses + self._ties}.
----------------------------------\
"""
        )

    def _win_or_lose(cmp: int) -> WinOrLose:
        match cmp:
            case 1:
                return WinOrLose.WIN
            case -1:
                return WinOrLose.LOSE
            case _:
                return WinOrLose.TIE

    def _loop(self):
        for _ in range(self._num_rounds):
            player_hand = reader.read_hand()
            if not player_hand:
                return

            computer_hand = rand.random_hand()

            print(
                f"Your hand: {player_hand},",
                f"computer hand: {computer_hand} ->",
                sep="",
                end="",
            )

            cmp = compare_hands(player_hand, computer_hand)
            wol = Game._win_or_lose(cmp)
            match wol:
                case WinOrLose.WIN:
                    self._wins += 1
                    print("You win!")
                case WinOrLose.LOSE:
                    self._losses += 1
                    print("You lose!")
                case _:
                    self._ties += 1
                    print("Tie.")

            self._end_round()
