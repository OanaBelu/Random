# Proiect 1 Number Guesser

import random

print("Hi! Welcome to the guessing game. Please guess a number between 1 and 100 ")
guess = int(input("What is your guess ?: "))
correct_number = random.randint(1, 100)
guest_count = 1

while guess != correct_number:
    guest_count += 1
    if guess < correct_number:
        guess = int(input("Wrong. You need to guess higher. What is your guess ?: "))
    else:
        guess = int(input("Wrong. You need to guess lower. What is your guess ?: "))
print(f"You got the right number {correct_number} . It took you {guest_count} guesses:) ")
