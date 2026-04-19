def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        guessed = [l if l in guesses else '_' for l in secret_word ]
        guessed_display = ''.join(guessed)
        print(guessed_display)
        if guessed_display == secret_word:
            return True
        else:
            return False       
    return hangman_closure

secret = input("secret word: ")
game = make_hangman(secret)
guess = input("guess a letter: ")

while not game(guess):
    guess = input("now let's guess a letter: ")


