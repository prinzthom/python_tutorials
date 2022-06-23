from pickle import APPEND
from hangman_art import stages, logo
from hangman_words import word_list
import random
from random import choice

crt_wrd = random.choice(word_list)
wrd_lngth = len(crt_wrd)
play_again = True
tries=6
lost = False
print(logo)
print(f"the word is {crt_wrd} ")
print(" ")

dsp_msg=[]
for _ in range(wrd_lngth):
    dsp_msg+="_"

while play_again:

    while lost is False:

        guessed_wrds=""
        tries = 6
        guess = input("Guess a letter: ").lower()


        if guess in guessed_wrds:
            print(f"You've already guessed {guess}")


        while tries > 0:
            dsp_msg = ""

            for _ in range(wrd_lngth):
                letter = crt_wrd[_]
                if letter == guess:
                    dsp_msg[_] = letter

            if guess not in crt_wrd:
                print(f"You guessed {guess}, that's not in the word. You lose a life.")   
                tries -= 1

                if tries == 0:
                    print("You lose the word was", end=f"{crt_wrd}")
                    lost = True

            if dsp_msg == crt_wrd:
                print("You Win!")
                
            print(dsp_msg)
            guess = ""
            while guess == "":
                print("You have", tries - 1, "guesses left.")
            guess = guess[0]
            guessed = guessed + guess

            for _ in guess:
                if guess not in crt_wrd:
                    tries = tries - 1
                    stages -=1
            print (stages)

    play_again = input("would you like to play again? (y/n): ")
    if play_again == 'n':
        play_again = False
        print('Thank you for playing.')
    else:
        play_again = True
from hangman_art import stages
print(stages[tries])
