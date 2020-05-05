import random

choices = ['python', 'java', 'kotlin', 'javascript']
correct = random.choice(choices)
correct_length = len(correct)
# removed = correct[3:correct_length]
# rem_num = len(removed)
modified_string = correct.rstrip(removed)


print("H A N G M A N")
# print(f"Guess the word {modified_string}" + "-" * rem_num + ": > ", end='')
print(f"Guess the word " + "-" * correct_length + ": > ", end='')
word = input()

if word == correct:
    print("You survived!")
else:
    print("You are hanged!")
