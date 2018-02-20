#
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else: # a guess must be greater than number
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")
import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}, or enter 0 to quit: ".format(highest))
# guess = int(input())
guess = 0 # initialize to any number outside of the valid range
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    elif guess < answer:
        print("Please guess higher")
    elif guess > answer: # a guess must be greater than number
        print("Please guess lower")
    else:
        print("Great, you guessed!")


