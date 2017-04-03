"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nLet's play a game")
    print("\nStart by picking a number")
    lower_bound = not_number_rejector("Enter a number: ")
    lower_bound = int(lower_bound)
    greater = False
    print("Now pick another number which is greater than {}  "
          "plus 1".format(lower_bound))
    while not greater:
        upper_bound = not_number_rejector("Enter number : ")

        if upper_bound > lower_bound + 1:
            greater = True
        elif upper_bound == lower_bound + 1:
            print("The number must be greater "
                  "than {} + 1 ".format(lower_bound))
        elif upper_bound == lower_bound:
            print("The number can't equal {}, try again".format(lower_bound))
        else:
            print("That number is not greater "
                  "than {}, try again ".format(lower_bound))
    upper_bound = int(upper_bound)
    guessed = False

    actual_number = random.randint(lower_bound + 1, upper_bound - 1)
    print("Now guess a number   ")

    while not guessed:
        guessed_number = super_asker(lower_bound, upper_bound)
        guessed_number = int(guessed_number)
        print("you guessed {}".format(guessed_number))
        if guessed_number == actual_number:
            print("You got it!!")
            guessed = True
        elif guessed_number < actual_number:
            print("Too low, try again")
        else:
            print("Too high, try again")
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
