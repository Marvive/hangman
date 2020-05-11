import random
guess_word = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
hint = ['-' for i in range(len(guess_word))]
tries = 0
used_letters = []

print('H A N G M A N')
while tries < 8:
    print()
    print(''.join(hint))
    char = input("Input a letter:")
    if char in used_letters:
        tries += 1
        print("No improvements")
        continue
    if char in guess_word:
        for i, v in enumerate(guess_word):
            if char == v:
                hint[i] = v
                used_letters.append(char)
    else:
        print("No such letter in the word")
        tries += 1

if tries < 8:
    print("You Survived!")
else:
    print("You are hanged!")

# print('''Thanks for playing!
# We'll see how well you did in the next stage''')
