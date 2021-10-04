import random

def play(word, lives):
    word = getWord()
    lives = getLives()
    guessed = []
    bingo = False
    wordLines = ('_' * len(word))
    print("Hello brave one, it is time to play a game")
    while lives > 0 or bingo == False:
        display(lives)
        print(wordLines)
        guess = input(prints(1))
        guessed.append(guess)
        if guess == word:
            bingo = True
        elif guess == 'QUIT':
            quit()
        elif guess == restart:
            restart()
        elif len(guess) > 1 and guess in guessed:
            print("")
        elif guess





def quit():
    pass

def prints('1', '2'):
    pass

def menu():
    pass

def difficulty():
    pass

def restart():
    pass

def clear():
    pass

def getLives():
    pass

def getWord():
    pass

def display(lives):
    pass