print("Wecome to the love calculator;)")
name1 = input("What is your name? \n")
name2 = input("What is thier name? \n")
first_digit = 0
second_digit = 0
combined_name = name1 + name2
combined_name = combined_name.lower()

first_digit +=  combined_name.count("t")
first_digit +=  combined_name.count("r")
first_digit +=  combined_name.count("u")
first_digit +=  combined_name.count("e")

second_digit += combined_name.count("l")
second_digit += combined_name.count("o")
second_digit += combined_name.count("v")
second_digit += combined_name.count("e")
score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"your score is {score}") 
