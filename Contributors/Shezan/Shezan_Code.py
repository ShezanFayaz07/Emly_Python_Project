def getUserGuess():
    guess = input("Enter your guess: ").strip().lower()
    return guess

def validateGuess(guess):
    if len(guess) != 1 or not guess.isalpha():
        return False
    return True

def isRepeatedGuess(guess, guessed_letters):
    for letter in guessed_letters:
        if guess == letter:
            return True
    return False

def processGuess(guess, secret_word, guessed_letters, wrong_letters, attempts_left):
    for letter in secret_word:
        if guess == letter:
            guessed_letters.add(guess)
            print("Correct guess!")
            return guessed_letters, wrong_letters, attempts_left
    wrong_letters.add(guess)
    attempts_left -= 1
    print("Wrong guess!")
    return guessed_letters, wrong_letters, attempts_left