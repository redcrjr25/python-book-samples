import random


def to_string(hand: str) -> str:
    if hand == "r":
        return "Rock"
    elif hand == "p":
        return "Paper"
    elif hand == "s":
        return "Scissors"
    else:
        return ""


#Read a user input and convert it into r, p, or s.
user_hand: str
u: str = input("Rock(r), Paper (p), or Scissors(s)?").lower()
if u.startswith("r"):
    user_hand = "r"
elif u.startswith("p"):
    user_hand = "p"
elif u.startswith("s"):
    user_hand = "s"
else: 
    user_hand = ""

#Randomly pick one of the strings, r, p, and s.
computer_hand: str
r: int = random.randint(0, 2)
if r == 0: 
    computer_hand = "r"
elif r == 1:
    computer_hand = "p"
else: 
    computer_hand = "s"

print("You:" + to_string(user_hand) + 
       "-- Computer:" + to_string(computer_hand))


#Compare the two hands and print the result.
if user_hand == computer_hand:
    print("Tie")
elif (user_hand == "r" and computer_hand == "s" or
        user_hand == "p" and computer_hand == "r" or
        user_hand == "s" and computer_hand == "p"):
    print("You win")
else: 
    print("You lose")




