# Importing Dependencies
from hangman_art import stages, logo
from hangman_words import word_list
from random import choice

# Priting the Logo
print(logo)

# Defining Global variables
game_is_finished = False
lives = len(stages)-1

# Displaying the underlines!
chosen_word = choice(word_list)
word_length = len(chosen_word)

print(f"Shhhhhhhhhhhh....... The chosen word is {chosen_word}!")
display = []
for _ in range(word_length):
    display.append("_")

while not game_is_finished:
    guess = input("Guess the letter: ").lower()

    if guess in display:
        print(f"You have already guessed '{guess}'")

    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print("That letter is not the the word! You lose a life!")
        lives -= 1
        if lives == 0:
            print("You Lose! That's the word:", chosen_word)
            game_is_finished = True

    if "_" not in display:
        print("You Win! That's the word:", chosen_word)
        game_is_finished = True

    print(stages[lives])