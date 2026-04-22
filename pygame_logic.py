import pygame
import random


font_big = pygame.font.SysFont('Arial', 80)
font_medium = pygame.font.SysFont('Arial', 46)
font_small = pygame.font.SysFont('Arial', 34)


# ===================================================================
# ===================================================================
# def initializeGameState(selected_word, guessed_letters, WordsList , attempts_left , wrong_letters):
    
#     selected_word = getRandomWord(WordsList)
#     guessed_letters = set()
#     attempts_left = 6
#     wrong_letters = set()

#     # print(f"{Yellow}Game Initialization Done, Random Word Is Selected\n")

#     return selected_word, guessed_letters, attempts_left, wrong_letters

# ===================================================================
# ===================================================================



def initializeGameState(selected_word, WordsList , attempts_left):
    
    selected_word = getRandomWord(WordsList)
    attempts_left = 6

    # print(f"{Yellow}Game Initialization Done, Random Word Is Selected\n")


    # intialize_text = "Game Initialization Done, Random Word Is Selected"
    # display_initialization_text = font_small.render(intialize_text, True, (255, 255, 255))
    # WIN.blit(display_initialization_text, (1200//2 - display_initialization_text.get_width()//2, 400))

    initialize_message = "Game Initialization Done, Random Word Is Selected"

    return selected_word, attempts_left, initialize_message




def getRandomWord(WordsList):
    return random.choice(WordsList)




def displayWordProgress(WIN, word, guessed_letters, attempts_left):
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += " " + letter + " "
        else:
            progress += " x "

    progress = progress.strip()
    display_word = font_small.render(progress , True, (255, 255, 255))
    WIN.blit(display_word, (1200//2 - display_word.get_width()//2, 500))

    attempts_left_str = str(attempts_left)
    attempts_text = font_small.render(attempts_left_str, True, (255, 255, 255))
    WIN.blit(attempts_text, (1200//2 - attempts_text.get_width()//2, 550))



def getUserGuess(WIN, guessed_letters, Wrong_letters , guess):
    
    guess = guess.strip().lower()

    if validateGuess(guess):        
        if isRepeatedGuess(guess, guessed_letters, Wrong_letters):
            validation_message = "You have already guessed that letter. Try a different one."
            return False,  validation_message
        else:
            return guess , ""
    else:
        validation_message = "Invalid input. Please enter a single letter (a-z)."
        return False , validation_message



def validateGuess(guess):
    if len(guess) != 1 or not guess.isalpha():
        return False
    return True

def isRepeatedGuess(guess, guessed_letters, Wrong_letters):
    for letter in guessed_letters.union(Wrong_letters):
        if guess == letter:
            return True
    return False


def processGuess(WIN , guess, secret_word, guessed_letters, wrong_letters, attempts_left):
    for letter in secret_word:
        if guess == letter:
            guessed_letters.add(guess)
            message_processedGuess = "Correct Guess!"
            return guessed_letters, wrong_letters, attempts_left , message_processedGuess
    wrong_letters.add(guess)
    attempts_left -= 1
    message_processedGuess = "Wrong Guess!"
    return guessed_letters, wrong_letters, attempts_left , message_processedGuess