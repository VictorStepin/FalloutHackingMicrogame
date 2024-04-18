from random import randrange

def create_words():
    words = ["Tom", "Pot", "Rot"]
    return words

def choose_word_to_guess(words):
    random_index = randrange(0, len(words))
    wordToGuess = words[random_index]
    return wordToGuess

def print_list(list):
    i = 0
    while i < len(list):
        print(list[i])
        i += 1

print("Welcome to Fallout Hacking Microgame")

words = create_words()
guess_word = choose_word_to_guess(words)
print_list(words)
print(guess_word)