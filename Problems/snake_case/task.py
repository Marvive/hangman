
word = input()

new_word = ""
for chars in word:
    if chars.isupper():
        new_word += f"_{chars.lower()}"
    else:
        new_word += chars

print(new_word)
