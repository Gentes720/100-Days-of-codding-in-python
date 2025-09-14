import math as m
# def greeet(name, location):
#     print("Hello, welcome to cersa cephar "+name)
#     print(f"you do you do {name} ??")
#     print(f"you live in {location}")

def numberOfCans (hight,width,coverage=5):
    return m.ceil((hight*width/coverage) )
#greeet("Angelin", "Napoli")
#print(f" you'll need {numberOfCans(5,5)} cans")

def prime_checker(n):
    isPrime = True
    for i in range (2, n):
        if n % i == 0 :
            isPrime = False
    if isPrime :
        print("is Prime")
    else:
        print("isn't prime")

#prime_checker(510)

   
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encrypt(word, shift, direction):
    encrypted = ""
    if direction == "decode":
        shift*= -1
    for letter in word:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift)% 26
            encrypted += alphabet[new_position]
        else:
           encrypted += letter
    print(f"this is the {direction} result : {encrypted}")


from asciiart8 import logo
print (logo)
choice = "yes"
while choice == "yes":
    direction = input("enter 'encorde' to encrypt of 'decode' to decrypt :\n")
    word = input(f"Enter the word you want to {direction}: \n").lower()
    shift = int(input("enter the shift number: \n"))
    encrypt(word, shift, direction)
    choice = input("Enter 'yes' to go again:  ")

