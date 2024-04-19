from random import randrange

def create_words():
    words = read_file_lines("words.txt")
    words = [word.strip('\n') for word in words]
    return words

def read_file_lines(file_path):
    lines = None
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines

def choose_secret_word(words):
    random_index = randrange(0, len(words))
    word_to_guess = words[random_index]
    return word_to_guess

print("Welcome to Fallout Hacking Microgame")

words = create_words()
secret_word = choose_secret_word(words)
print(words)
print(secret_word)

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