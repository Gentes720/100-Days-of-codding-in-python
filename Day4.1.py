import random

names_string = input("Give me every body's name, separated by a comma.")

names = names_string.split(",")
print(names[random.randint(0, len(names)-1)]," will pay the bill")