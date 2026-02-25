
#THIS REQUIRES WONDERWORDS: https://pypi.org/project/wonderwords/

#hangman logic:

#  generate a random word

# Ask user for input

# verify if userInput is present in the random word
# If it is, store the letter on a list with index and store the guessed letter and add correct point
# If its not, remove one chance from the chances and store the guessed letter

# if user have no more chances, end game
# if user found all letters, win the game


# GAME IS WORKING: ROADMAP:
# - Difficulty levels
# - Menu with selections
# - Word Mode


from wonderwords import RandomWord

ww = RandomWord()

generated_word = ww.word(word_min_length = 5, word_max_length = 5)      #generating a random word of 5 letters
allguesses = ' '
playing = 0
correct = 0
chances = len(generated_word) + 3

# print(generated_word)
word = ['_'] * len(generated_word)

while playing == 0:    
    try:
        try:    
            user_guess = input("Type a letter:")
        except:
            print("Please insert only one letter")

        # Verify input
        if not user_guess.isalpha():
            print("Input only ONE LETTER")
        elif len(user_guess) > 1:
            print("Input only ONE LETTER")
        elif user_guess in allguesses:
            print("Already guessed this letter")
       
        #verify if user guess is on the word
        if user_guess in generated_word and user_guess not in allguesses:

            for index in range(len(generated_word)):
                if generated_word[index] == user_guess:
                    word[index] = user_guess
                    correct += 1
            
            print("letter found")
            allguesses += user_guess

        else:
            print(f"No {user_guess} in the secret word")
            allguesses += user_guess
            chances-=1

        if correct == len(generated_word):
            print("You got it!")
            print(f"The word was: {word}")
            break

        # End game if 0 chances
        if chances <=0:
            print("Game over, you didn't found the secret word")
            print(f"The Secret word was: {generated_word}")
            playing = 1
            break
        
        print(word)

    except KeyboardInterrupt:
        print()
        print("Leaving...")
        quit()
