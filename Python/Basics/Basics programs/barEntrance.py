# Welcome to MikuBar!

print("*u* Welcome to ()Oo. Mikubar .oO()!")
userName = input("Please tell me your name: ")
userAge = int(input("What is your age? "))

if userName == " ":
    print("Your name can't be empty space, leave!")
if userAge >= 18:
    print(f"Welcome {userName}, Please come in!")
elif userAge < 18:
    print("I'm sorry but you are not old enough for miku bar!")
