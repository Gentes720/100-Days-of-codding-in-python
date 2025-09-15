from asciiart8 import logo131
from asciiart8 import logo132
from data import celebrities
from random import randint
import os

already_chosen = []
def new_celeb():
    a = randint(0, 51)
    while a in already_chosen:
        a = randint(celebrities)
    already_chosen.append(a)
    return a
lose = False

print(logo132)
A = new_celeb()
B = new_celeb()
counter = 0
print("A :",celebrities[A]['nom_celeb'], "\n",celebrities[A]['description'],"From",celebrities[A]['pays_origine'], celebrities[A]['followers_instagram'],'\n')
print(logo131)
print("A :",celebrities[B]['nom_celeb'], "\n",celebrities[B]['description'],"From",celebrities[B]['pays_origine'])
choice = input("Who is more popular 'A' OR 'B' ?? ")
if choice == "A" and celebrities[A]['followers_instagram'] > celebrities[B]['followers_instagram'] :
    print(" Good")
    counter += 1
    os.system("clear")
elif choice == "B" and celebrities[A]['followers_instagram'] < celebrities[B]['followers_instagram'] :
        print(" Good")
        counter += 1
        os.system("clear")
else:
    lose = True
    print(f"Sorry!!! your score is {counter}")
while lose == False :
    A = B
    B = new_celeb()
    print("A :",celebrities[A]['nom_celeb'], "\n",celebrities[A]['description'],"From",celebrities[A]['pays_origine'], celebrities[A]['followers_instagram'],'\n')
    print(logo131)
    print("A :",celebrities[B]['nom_celeb'], "\n",celebrities[B]['description'],"From",celebrities[B]['pays_origine'])
    choice = input("Who is more popular 'A' OR 'B' ?? ")
    if choice == "A" and celebrities[A]['followers_instagram'] > celebrities[B]['followers_instagram'] :
        print(" Good")
        counter += 1
        os.system("clear")
    elif choice == "B" and celebrities[A]['followers_instagram'] < celebrities[B]['followers_instagram'] :
        print(" Good")
        counter += 1
        os.system("clear")
    else:
        lose = True
        print(f"Sorry you lose !!! your score is {counter}")
