import random

SECRET_NUMBER = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10: "))

while guess != SECRET_NUMBER:
    print("you got it wrong. Try again!")
    guess = int(input("Guess another number between 1 and 10: "))

print("you got it! You win!")
