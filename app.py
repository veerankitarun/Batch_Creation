import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 10 \n")
    guess = int (guess)
    if guess == num:
        print("congratulation! you won!")
        break
    else:
        print("nope, sorry. try again!")