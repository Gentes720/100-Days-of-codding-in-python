#import the ascii art
from asciiart8 import logo12
import random
# asign the random number

guess_number = random.randint(1, 100) 
attempts = 0
# ask and asign difficulty
difficulty = input(" Enter the difficulty 'hard' or 'easy'")
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5
# creae the program counter
while attempts > 0 :
    choice = int(input("Guess the number : "))
    if choice > guess_number:
        print("It's less")
    elif choice < guess_number:
        print("It more")
    else:
        print(f"CONGRATS the number is {choice}")
        break 
    attempts -= 1
    print(f" {attempts} attempts remaining")

print(f" you lose, the number was {guess_number}")