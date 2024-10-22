lives = 10
word = 'apple'
letters = list(word.lower())
stars = '*' * len(letters)

def calculateLives():
    global lives
    lives -= 1
    print('You have ' + str(lives) + ' lives left.')
    return lives

#create input with the text about hidden word and ***** as word to guess
def welcomeMessage():  
    print(f'Welcome to the game of Hangman! You have {lives} lives to guess the word "{stars}". Press enter to start.') 

def getLetter():
    guess = input('Enter a letter: ')
    return guess
welcomeMessage()

#check if the letter is in the word
def checkLetter():
    global stars
    global lives
    while '*' in stars and lives > 0:
        userLetter = getLetter()
        if userLetter in letters:
            print(f'The letter "{userLetter}" is in the word.')
#replace the * with the letter
            for i in range(len(letters)):
                if userLetter == letters[i]:
                    stars = stars[:i] + userLetter + stars[i+1:]
                    print(stars)
        elif userLetter not in letters:
            print(f'The letter "{userLetter}" is not in the word.')
            lives = calculateLives()
            if lives == 0:
                print(f'You have run out of lives. The word was "{word}".')
                break
#check if the word is complete
    else:
        if '*' not in stars:
            print('Congratulations! You have guessed the word.')
checkLetter()


