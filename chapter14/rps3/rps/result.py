from enum import Enum

class WinOrLose(Enum):
    WIN, LOSE, TIE = 1, -1, 0

    def __str__(self) -> str:
        match self:
            case WinOrLose.WIN:
                return "Win"
            case WinOrLose.LOSE:
                return "Lose"
            case WinOrLose.TIE:
                return "Tie"
            case _:
                raise ValueError
