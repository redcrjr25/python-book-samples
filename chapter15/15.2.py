# Lab 15.2 I'll be going...

import random
from enum import Enum

class CardinalDirection(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    def __str__(self):
        direction_map = {
            CardinalDirection.NORTH: "north",
            CardinalDirection.EAST: "east",
            CardinalDirection.SOUTH: "south",
            CardinalDirection.WEST: "west",
        }
        return direction_map[self]

def pick_random_direction():
    # Randomly select a direction from CardinalDirection enum
    direction = random.choice(list(CardinalDirection))
    return f"I have nothing to do today.\nI'll be going to the {direction}, as the wind blows:)"

def main():
    for _ in range(7):
        print(pick_random_direction())

if __name__ == "__main__":
    main()
