"""
File: dice.py
Description: Simulates the dice game of craps and reports
             the number of player wins and the maximum
             number of rolls in any round.
Assignment Number: 6

Name: Michael Abiwu
SID: 2425402790
Email: abiwuamk17@gmail.com
Grader: Augustus Buckman

On my honor, Michael Abiwu, this programming assignment is my own work
and I have not provided this code to any other student.

"""
import random

print("This program simulates the dice game of craps.")

choice = input("Do you want to set the seed? Enter y for yes, anything else for no: ")

if choice == "y":
    seed_value = int(input("Enter an int for the initial seed: "))
    random.seed(seed_value)

rounds = int(input("Enter the number of rounds to run: "))

if rounds <= 0:
    print("Number of rounds must be greater than 0.")
else:
    wins = 0
    max_rolls = 0

    round_num = 0

    while round_num < rounds:

        roll_count = 1

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        if total == 7 or total == 11:
            wins += 1

        elif total == 2 or total == 3 or total == 12:
            pass

        else:
            point = total
            done = False

            while not done:
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                total = die1 + die2
                roll_count += 1

                if total == point:
                    wins += 1
                    done = True
                elif total == 7:
                    done = True

        if roll_count > max_rolls:
            max_rolls = roll_count

        round_num += 1

    if wins == 1:
        win_word = "time"
    else:
        win_word = "times"

    if rounds == 1:
        round_word = "round"
    else:
        round_word = "rounds"

    print("Player won", wins, win_word, "in", rounds, round_word + ".")
    print("Maximum number of rolls in a round =", max_rolls)

# Questions:
#
# 1. Does the simulation support the idea that in the long run,
#    casinos come out the winner? Why or why not?
#
#    Yes. The simulation shows that the player wins slightly less
#    than 50% of the rounds over a large number of games. Because
#    the casino has a small statistical advantage, the casino is
#    expected to make money in the long run.
#
# 2. Assume you have $2,000. You can simply keep the money or play
#    craps. If you play craps, each round you must bet $10 and you
#    must play until you run out of money or have completed 500 games.
#    Would you choose to keep the $2,000 and not play or play craps
#    as described? Why or why not?
#
#    I would keep the $2,000. Although it is possible to win money,
#    the odds favor the casino in the long run. Keeping the money
#    guarantees that I do not lose any of it.