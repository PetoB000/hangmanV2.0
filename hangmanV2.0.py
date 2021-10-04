import random
import os

def play(word, lives):
    bingo = False
    wordLines = ('_' * len(word))
    guessed = []
    while lives > 0 and bingo == False:
        #display(lives)
        print(wordLines)
        guess = input("A").upper()
        #clear()
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

def getWelcomeMessage():
    messages = ["Welcome brave one! Think you can outsmart me?\nWe will see about that",
                "Coming back for a round 2 huh? I'm in",
                "Aren't you getting tired yet?",
                ]
    return messages


def quit():
    pass

def prints():
    pass


def menu():
    welcomeMessage = getWelcomeMessage()
    tries =
    while True:
        if tries == 0:
            print(welcomeMessage[0])
        elif tries == 1:
            print(welcomeMessage[1])
        else:
            print(welcomeMessage[2])
        choice = input("")

def difficulty():
    pass

def restart():
    option = input("Do you want to play again?\n(Y/N)").upper()
    if option == "Y":
        choice = input("Do you want to change settings?\n(Y/N)").upper()
        if choice == "Y":
            menu()
        elif choice == "N":
            play(word, lives)
    else:
        quit()

def clear():
    pass

def getLives(choice):
    if choice == '1':
        lives = 6
    if choice == '2':
        lives = 3

def getWord():
    pass

def display(lives):
    pass

if __name__ == '__main__':
    menu()