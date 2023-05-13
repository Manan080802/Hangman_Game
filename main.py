from replit import clear
import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

# word_list1 = word_list
word = random.choice(word_list)
# print(word)
lives = 0
empty = []
for i in range(0, len(word)):
    empty += "_"
lives = 6
while True:
    print(f"{empty} \n")
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in empty:
        print(f"You've already guessed {guess}")

    for postion in range(len(word)):
        check = word[postion]
        if (check == guess):
            empty[postion] = guess

    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            print("You Lose")
            break

    if "_" not in empty:
        print(f"{empty} \n You win.")
        break

    print(stages[lives])
