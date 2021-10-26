
from random import randint


def guess(attempts, numrange):
    number = randint(1, numrange)
    print("Welcome! Can you guess my secret number?")

    while(attempts > 0):
        guessing = int(input("Please input your guessing number: "))
        attempts -= 1
        if guessing == number:
            print("Well done! you got it right.")
            break
        elif guessing > number:
            print("No - too high!")
        elif guessing < number:
            print("No - too low!")

        if attempts > 0:
            print("You have", attempts, "remaining")
        else:
            print("No more guesses - bad luck!")
    # YOUR CODE GOES HERE!

    print("END-OF-GAME: thanks for playing!")


if __name__ == "__main__":
    guess(4, 20)
    pass
