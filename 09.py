from asciiart8 import logo1
import os


# numbers = {
#     '1':'one',
#     '2':'two',
#     '3':'three'
# }
# print(numbers['1'])
# numbers['4'] = 'four'
# print(numbers)
# for thing in numbers:
#     print(numbers[thing])

# students_scores = {
#     'One': 81,
#     'two': 78,
#     'three': 99,
#     'four': 74,
#     'five': 62

# }
# students_grades = {}
# for name in students_scores:
#     score = students_scores[name]
#     if score >= 91 :
#         students_grades[name] = 'Outstanding'
#     elif score >= 81 :
#         students_grades[name] = 'Exceed expectations'
#     elif score >= 71 :
#         students_grades[name] = 'Acceptable'
#     else:
#         students_grades[name] = 'failed'

# print(students_grades)

# travel_log = [
#     {
#         'country': 'france',
#         'visits': 12,
#         'cities': ['Paris', 'Lille', 'Dijon']
#     },
#     {
#         'country': 'Germany',
#         'visits': 5,
#         'cities': ['Berlin', 'Hamburg', 'Stuttgart']
#     },
# ]
# print(travel_log[0]["country"])
# print(travel_log[0]["cities"][2])
other_player = 'yes'
bids = {}
while other_player == 'yes': 
    print(logo1)
    print("Welcome to the secret auction program")
    name = input("What is your name?? ")
    bid = int(input("what's your bid??  $"))
    bids[name] = bid
    other_player = input("Are there other bidders? type 'yes' on 'no'.")
    os.system('clear')
max = 1
for name in bids:
    if bids[name] >= max:
        max = bids[name]
        winner = name
print(f"{winner} won with a bit of ${max} \n {bids}")
