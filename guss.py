import random

number = random.randint(1, 10)

print("Guess the number (1 to 10)")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("Correct! You guessed the number 6")
        break