
# Guessing Game:
# Guess the number
# Limited Attempts
# Difficult selector

import random

easy = 10
normal = 50
hard = 100
custom = 0


def numberGen(poolsize):
    number  = random.randrange(0,poolsize)
    return number

def main():
    
    lives = 0

    print("Welcome to the Guessing game 2026")
    print("To start off, what difficult would you like to play?")
    print("1. Easy, 2. Normal, 3. Hard, 4. Custom")

    player_difficult_selector = int(input())

    match player_difficult_selector:
        case 1:
            game_pool = easy
            lives = 8
        case 2:
            game_pool = normal
            lives = 5
        case 3:
            game_pool = hard 
            lives = 3
        case 4:
            game_pool = int(input("Type the ammount of numbers: "))
            lives = 5

    randNumber = numberGen(game_pool)

    print("Lets start the game, Type the number you think I decided:")
    print(f"Guessing Chances: {lives}")

    while lives > 0:
        print(f"Guessing Chances: {lives}")
        player_guess = int(input("Type your guess:"))

        if player_guess == randNumber:
            print("You guessed right!")
            break
        if player_guess > randNumber:
            print("Your guess is Bigger!")
            lives-=1
        elif player_guess < randNumber:
            print("Your guess is Lower!")
            lives-=1
        
        if lives <=0:
            print("Runned out of Chances! better luck next time!")
    
main()