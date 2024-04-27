secret_word = "Sora"
guess = ""
i = 0

while (guess != secret_word) and (i <= 4):
    guess = input("What is the secret word? Take a guess: ")
    i += 1

if (guess == secret_word):
    print("Well done, mate!")
else:
    print("Well, you tried brother.")
