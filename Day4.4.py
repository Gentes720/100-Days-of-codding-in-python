import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        ''')
paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
         ''')
scissors = ('''
      _____
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

list = [rock, paper, scissors]

my_choice = int(input("what do you choose? Type 0 for Rock, 1 for paper or 2 for scissors "))
if my_choice == 0:
    print(rock)
elif my_choice == 1:
    print(paper)
elif my_choice == 2:
    print(scissors)
else:
    my_choice = random.randint(0, 2)
    print(list[my_choice])


pc_choice = random.randint(0,2)
print("the computer chose\n",list[pc_choice])
result_table = [["Equal", "You WIN", "You Lose"], ["You Lose", "Equal", "You win"], ["You win", "You Lose", "Equal"]]
print(result_table[pc_choice][my_choice])
# pc_choice is the row and my choice is the line then we use this table
#          R    P    S
#          0    1    2
#      R 0 Equ  Win  Lose
#      P 1 Lose Equ  Win
#      S 2 Win  Lose Equal
#