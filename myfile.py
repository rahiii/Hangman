# Hangman
import random
Hangman_words = ["hat", "happy", "slides", "charger", "mice", "phone"]
word_length = len(Hangman_words)
random_index = random.randint(0, word_length-1)
word = Hangman_words[random_index]
word_length = len(word)

print("lets play hangman!Your word has", len(word), "letters")
#blank = "_ " * len(word)
#print(blank)
wrong = []
guesses_left = 10
blank = []

for i in range(len(word)):
    blank.append("_")
print(blank)

while guesses_left > 0 and "_" in blank:
    user_guess = raw_input("Guess a letter ")
    if user_guess in word:
        for i in range(len(word)):
            if user_guess == word[i]:
                blank[i] = user_guess
    elif user_guess in wrong:
        print("You already guessed that letter")
    else:
        wrong.append(user_guess)
        guesses_left -= 1
    print(wrong)
    print(guesses_left)
    print(blank)
