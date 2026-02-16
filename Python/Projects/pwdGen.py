
# Password Generator
#
# - choose size
# - Letter, letters and number, letters number and Symbols Options
# - Uppercase / lowercase 

import random

lettersLOW = list("abcdefghijklmnopqrstuvwxyz")
lettersUP = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
special = ['!','@','#','$','%','&','*','(','/','-','_']


def passwordGenerator(ptype,psize):
    password = ""
    match ptype:
        case 1:
            pool = lettersLOW + lettersUP
        case 2:
            pool = lettersLOW + lettersUP + numbers
        case 3:
            pool = lettersLOW + lettersUP + numbers + special
    
    for size in range(0,psize):
        password+= random.choice(pool)
    print(password)

def main():
    print("Welcome to the PassGen")
    print("Select the type of password")
    print("1: Letters only")
    print("2: Letters and Numbers")
    print("3: Letters, Numbers and Special")
    passwordType = int(input())

    print("Please type the size of the password:")
    passwordSize = int(input())
    passwordGenerator(passwordType,passwordSize)

main()

