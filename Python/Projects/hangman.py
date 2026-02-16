
# hangman game 
#
# 3 difficults
#  easy = 5 letter words
# normal = 5 to 12 letter words
# hard = 8 to 12 letter words

#word pool
from wonderwords import RandomWord



def randomWord(size):
    random_word = RandomWord().word(word_min_length = size,word_max_length = size)
    guess_word = random_word
    return guess_word


def hangman(word):

    guess_word = word

    guessed=[]
    trys = []
    answer = guessed
    print(answer)
    while True:
        guess = input()
        trys.append(guess)
        for index in range(0,len(guess_word)):
            if guess_word[index] == guess:
                guessed.insert(index,guess)
        print(guessed)

        if answer == guess_word:
            break
    
    print(guess_word,guessed)
        

def main():
    generated_word = randomWord(8)
    print(generated_word)
    hangman(generated_word)
    



main()
