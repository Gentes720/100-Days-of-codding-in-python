print("Welcome to pizza deliveries!")
size = input("What size of pizza do you want? S, M, L")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "s" :
    bill += 15 
elif size == "l":
    bill += 20
else:
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"your final bill is ${bill}")
