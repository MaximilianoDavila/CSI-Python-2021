import random
word_list = ["areyto", "batata", "batea", "barbacoa", "arepas", "batu", "bohique", "boriken", "huracan", "arepa"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("let's play Hangman, everybody's favorite game and the most that requires you being intellectual.")
    print("theme: Taino words")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("that word is already tried, pick another", guess, "!")
            elif guess not in word:
                print("Isn't in the word :(, I believe in you still.")
                tries -= 1
                guessed_letters.append(guess)


def display_hangman(tries):
    stages = [ """
                    -------- 
                    |    |   
                    |    0
                    |   /|\\
                    |    |
                    |   / \\
                    -
                    """,
                    """
                    -------- 
                    |    |   
                    |    0
                    |   /|\\
                    |    |
                    |   / 
                    -
                    """,
                    """
                    -------- 
                    |    |   
                    |    0
                    |   /|\\
                    |    |
                    |    
                    -
                    """,
                    """
                    -------- 
                    |    |   
                    |    0
                    |   /|
                    |    |
                    |    
                    -
                    """,
                    """
                    -------- 
                    |    |   
                    |    0
                    |    |
                    |    |
                    |    
                    -
                    """,
                    """
                    -------- 
                    |    |   
                    |    0
                    |    
                    |    
                    |    
                    -
                    """,
                    """
                    -------- 
                    |    |   
                    |    
                    |    
                    |    
                    |    
                    -
                    """,
]