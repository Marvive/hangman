import random
guess_word = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
hint = ['-' for i in range(len(guess_word))]
tries = 0
used_letters = []


def start_menu():
    print('H A N G M A N')
    start = input('Type "play" to play the game, "exit" to quit:')
    if start.lower() == "exit":
        exit()
    elif start.lower() != "play":
        start_menu()


start_menu()

while tries < 8:
    hint_output = ''.join(hint)
    if '-' not in hint_output:
        break
    print()
    print(hint_output)
    char = input("Input a letter:")

    if len(char) != 1:
        print("You should print a single letter")
        continue
    elif char in used_letters:
        print("You already typed this letter")
        continue
    elif char.isupper() or not char.isalpha():
        print("It is not an ASCII lowercase letter")
        continue

    if char in guess_word:
        for i, v in enumerate(guess_word):
            if char == v:
                hint[i] = v
                used_letters.append(char)
    else:
        print("No such letter in the word")
        used_letters.append(char)
        tries += 1

if tries < 8:
    print("You Survived!")
else:
    print("You are hanged!")
