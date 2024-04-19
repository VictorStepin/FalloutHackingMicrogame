from random import randrange

def create_words():
    words = ["Tom", "Pot", "Rot"]
    return words

def choose_secret_word(words):
    random_index = randrange(0, len(words))
    wordToGuess = words[random_index]
    return wordToGuess

print("Welcome to Fallout Hacking Microgame")

words = create_words()
secret_word = choose_secret_word(words)
print(words)

win = False
attempts_count = 4
attempt = 0
while attempt < attempts_count:
    print("Attempts left: " + str(attempts_count - attempt))
    attempt += 1
    guess = input("Enter a word: ")
    if guess == secret_word:
        win = True
        break
    else:
        if attempt != attempts_count:
            print("Wrong, try again")
    print()

if win:
    print("You win!")
else:
    print("You lose.")