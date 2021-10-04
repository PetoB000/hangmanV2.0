import random
import os

def play(word, lives):
    bingo = False
    wordLines = ('_' * len(word))
    guessed = []
    print("Hello brave one, it is time to play a game")
    while lives > 0 and bingo == False:
        #clear()
        #display(lives)
        print(wordLines)
        guess = input("A").upper()
        guessed.append(guess)
        if guess == word:
            print("Wow, You're really good!")
            bingo = True
            #restart()
        elif guess == 'QUIT':
            quit()
        elif guess == "RESTART":
            restart()
        elif len(guess) > 1 and guess != word:
            print("Thats not the right one")
        #elif guess in guessed:
            #print(prints(2))
        elif guess in word:
            listedWord = list(wordLines)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                listedWord[index] = guess
            wordLines = "".join(listedWord)
            #print(prints(3))
        else:
            #prints(4)
            lives -= 1
            print("You can try " + str(lives), "more times")
        if "_" not in wordLines:
            if lives > 0:
                print("Good job, you guessed it!")
            bingo = True
            #restart()
        if lives == 0:
            print("Better luck next time")
            #restart()



def quit():
    pass

def prints():
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

if __name__ == '__main__':
    play(word, lives)