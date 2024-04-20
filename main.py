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

def count_matches(secret_word, word_to_compare):
    matches = sum(a == b for a, b in zip(secret_word, word_to_compare))
    return matches

print("Welcome to Fallout Hacking Microgame")

words = create_words()
secret_word = choose_secret_word(words)
print(words)
#print(secret_word)

win = False
attempts_count = 4
attempt = 0
while attempt < attempts_count:
    print(f"Attempts left: {attempts_count - attempt}")
    attempt += 1
    guess = input("Enter a word: ")
    if guess == secret_word:
        win = True
        break
    else:
        if attempt != attempts_count:
            matches = count_matches(secret_word, guess)
            print(f"{matches}/{len(secret_word)} matched.")
    print()

if win:
    print("You win!")
else:
    print("You lose.")
