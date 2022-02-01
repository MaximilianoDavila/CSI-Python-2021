import random
word_list = ["areyto", "batata", "batea", "barbacoa", "arepas", "batu", "bohique", "boriken", "huracán", "arepa"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("let's play Hangman, everybody's favorite game and, also requires you to be intellectual with your guesses.")
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
            else:
                print("Nice one", guess,"is in the word, pick another one")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already tried, is another one, go ahead. Really go ahead.", guess, "!")
                elif guess != word:
                    print(guess, "sorry, that isn't in the word, go ahead and give another shot")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
        else:
            print("invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Good job!! you guessed the word correctly, it took me five years to do this game. Avoiding that fact, Congratulation!! now take my advice coding is very hard, never underestimate it.")
    else:
        print("im terriby sorry put you lost, though I hope you enyoyed it. Ohh btw the word was" + word + ". try your skills again, there is no problem in trying again.")


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
    return stages[tries]
def main():
    word = get_word(word_list)
    play(word)
    while input("Wanna try again? Or is that it for today champ? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ =="__main__":
    main()
