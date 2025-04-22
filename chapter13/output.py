def horz_bar():
    print("+" * 4 + "-" * 35 + "+" * 4)


def start_banner():
    horz_bar()
    print("Let's play Rock Paper Scissors!")
    horz_bar()


def end_banner(wins: int = 0, rounds: int = 0):
    print("Thanks for playing Rock Paper Scissors!")
    if rounds > 0:
        print(f">>> You won {wins} rounds out of {rounds}. <<<")
    horz_bar()


def print_result(user, computer, result):
    print(f"You -- {user} vs {computer} -- Computer")
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("Tie!")
