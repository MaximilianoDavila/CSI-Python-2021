import random
word_list = ["areyto", "batata", "batea", "barbacoa", "arepas", "batu", "bohique", "Bayamanaco", "Iguanaboina", "ItibaCahuba"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("let's play hangman")
    print("theme: taino words")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("already tried", guess, "!")
            elif guess not in word:
                print("Isn't in the word :)")
                tries -= 1
                guessed_letters.append(guess)


def display_hangman(tries):
    stages = [ """
                    -------- 
                    |
    ]