import random

num = random.randint(1, 20)
count = 0
n_guess=0
while n_guess != num:
    n_guess = int(input("Guess a number between 1 to 20 "))
    count += 1
    if n_guess < num:
        print("Guess a larger number.")
    if  n_guess > num:
        print("Guess a smaller number.")

print("you rock! You guessed the number")
print("You made ",count," guesses.")