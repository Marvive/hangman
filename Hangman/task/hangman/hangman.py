import random

choices = ['python', 'java', 'kotlin', 'javascript']
answer = random.choice(choices)
answer_length = len(answer)
answer_array = list(answer)
hidden_word = answer_length * "-"
hidden_word_array = list(hidden_word)
tries = 8
unsolved = True

print("H A N G M A N")
print(f"Guess the word " + hidden_word + ": > ", end='')

while tries > -1 and unsolved:
    attempt_word = input()
    if attempt_word in answer:
        print("Good Choice!")
        counter = 0
        for chars in answer:
            if chars == attempt_word:
                hidden_word_array[counter] = chars
            counter += 1
        hidden_word = ''.join(hidden_word_array)
    else:
        print("Bad Choice")
        if tries != 1:
            print(f"You have {tries} tries left.")
        else:
            print(f"You have 1 try left.")
        tries -= 1
    print(hidden_word)

if unsolved:
    print("You died!")
else:
    print("You live!")

