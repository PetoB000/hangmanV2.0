import random
import os


def play(diff, chances):
    word = get_word(diff)
    lives = get_lives(chances)
    word_lines = ('_' * len(word))
    guessed = []
    while lives > 0:
        clear()
        print(display(lives))
        print(word_lines)
        guess = input("Go on! Try guessing.\n").upper()
        if guess == word:
            print("Wow, You're really good!\n")
            restart()
        if len(guess) == 1 and guess.isalpha():
            if guess == 'QUIT':
                goodbyemsg()
            elif guess == "RESTART":
                restart()
            elif guess in guessed:
                print('You already guessed this letter "' + guess + '"')
            elif guess not in word:
                lives -= 1
                print('"' + guess + '" Is not in the word')
                if lives > 0:
                    print("You've got " + str(lives) + " lives left")
            elif guess in word:
                listed_word = list(word_lines)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    listed_word[index] = guess
                word_lines = "".join(listed_word)
            if "_" not in word_lines:
                print("Good job, you guessed it!")
                restart()
            if lives == 0:
                print("Better luck next time")
                restart()
            guessed.append(guess)


def menu():
    menu_logo()
    print("Oooh, you must be here to play a game with me. You got it!")
    print("_" * 81)
    option = int(input("You can change the settings by typing their number or play with default settings.\n"
                       "1. Let's play the game\n2. Check settings\t3. Quit\n"))
    if option == 1:
        play("2", "2")
    elif option == 2:
        settings()
    else:
        goodbyemsg()


def restart():
    option = input("Do you want to play again?\n(Y/N)").upper()
    if option == "Y":
        menu()
    elif option != "N":
        print("So scared cant type a valid input?...Pathetic")
    else:
        goodbyemsg()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_lives(chances):
    global life
    if chances == '2':
        life = 6
    elif chances == '1':
        life = 4
    return life


def settings():
    diff = input("Select a vocabulary:\n1. countries_and_capitals\t\t2. Basic vocabulary")
    if diff != '1' and diff != '2':
        print("Invalid input, choose '1' or '2'")
    vocabulary = input("Select a difficulty:\n1. Hard mode\t\t2. Easy mode")
    if vocabulary != '1' and vocabulary != '2':
        print("Invalid input, choose '1' or '2'")
    return play(diff, vocabulary)


def get_word(diff):
    global words
    if diff == "1":
        words = open("countries-and-capitals.txt", "r").read().split()
    else:
        words = ["rubbish", "family", "purpose", "location", "chain", "business", "plan"]
    return random.choice(words).upper()


def menu_logo():
    print(""""                                                                                                                
\t\t\t\t _   _                    ___  ___                 
\t\t\t\t| | | |                   |  \/  |
\t\t\t\t| |_| | __ _ _ __   __ _  | .  . | ___ _ __  _   _  
\t\t\t\t|  _  |/ _` | '_ \ / _` | | |\/| |/ _ \ '_ \| | | |
\t\t\t\t| | | | (_| | | | | (_| | | |  | |  __/ | | | |_| |
\t\t\t\t\_| |_/\__,_|_| |_|\__, | \_|  |_/\___|_| |_|\__,_|
\t\t\t\t                    __/ |                          
\t\t\t\t                   |___/                           
        """)


def goodbyemsg():
    print(""""
 _   _       _   _ _   _   _           _     _____ _                 
| | | |     | | (_) | | \ | |         | |   |_   _(_)                
| | | |_ __ | |_ _| | |  \| | _____  _| |_    | |  _ _ __ ___   ___  
| | | | '_ \| __| | | | . ` |/ _ \ \/ / __|   | | | | '_ ` _ \ / _ \ 
| |_| | | | | |_| | | | |\  |  __/>  <| |_    | | | | | | | | |  __/ 
 \___/|_| |_|\__|_|_| \_| \_/\___/_/\_\___|   \_/ |_|_| |_| |_|\___| 
        """)
    quit()


def display(lives):
    hangman = ["""
                   ________ 
                    |/   |  
                    |   (_) 
                    |   /|\ 
                    |    |  
                    |   / \ 
                    |       
                    |___    
                """,
               """
                   ________
                    |/   |     
                    |   (_)    
                    |   /|\           
                    |    |        
                    |   /         
                    |               
                    |___           
                """,

               """
                   _________              
                    |/   |                     
                    |   (_)                     
                    |   /|\                    
                    |    |                       
                    |                             
                    |                            
                    |___                          
                """,

               """
                   _________             
                    |/   |               
                    |   (_)                   
                    |   /|                     
                    |    |                    
                    |                        
                    |                          
                    |___                          
                """,

               """
                   ________               
                    |/   |                   
                    |   (_)                  
                    |    |                     
                    |    |                    
                    |                           
                    |                            
                    |___                    
                """,

               """
                   _________       
                    |/   |              
                    |   (_)
                    |                         
                    |                       
                    |                         
                    |                          
                    |___                       
                """,

               """
                   _________
                    |/   |      
                    |              
                    |                
                    |                 
                    |               
                    |                   
                    |___                 
                """]
    return hangman[lives]


if __name__ == '__main__':
    menu()
