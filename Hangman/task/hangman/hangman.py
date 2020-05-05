import random

choices = ['python', 'java', 'kotlin', 'javascript']
answer = random.choice(choices)
answer_length = len(answer)
# removed = answer[3:answer_length]
# rem_num = len(removed)
# modified_string = answer.rstrip(removed)
hidden_word = answer_length * "-"
tries = 8
unsolved = True

print("H A N G M A N")
# print(f"Guess the word {modified_string}" + "-" * rem_num + ": > ", end='')
print(f"Guess the word " + hidden_word + ": > ", end='')
word = input()

while tries > -1 and unsolved:
    attempt_word = input()
    if attempt_word in answer:
        print("Good Choice!")
    else:
        print("Bad Choice")
        tries -= 1

if word == answer:
    print("You survived!")
else:
    print("You are hanged!")

