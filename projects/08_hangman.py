from hangman_art import logo
from hangman_words import word_list
import random
from random import choice

play_again = True



print(logo)


while play_again:
    crt_wrd = random.choice(word_list)
    print(f"the word is ~{crt_wrd}~ ")
    wrd_lent = len(crt_wrd)
    dsp_msg = []
    tries = 6
    gssd_wrd = ""
    for _ in range(wrd_lent):
        dsp_msg += "_"

    while tries > 0:
        dsp_msg = ""

        for character in crt_wrd:
            if character in gssd_wrd or character == " ":
                dsp_msg = dsp_msg + character
            else:
                dsp_msg = dsp_msg + "_"

        print(dsp_msg)
        guess = ""
        while guess == "":
            guess = input("Guess a Letter: ").lower()
            print(f"You have {tries} tries left.")
        guess = guess[0]
        gssd_wrd = gssd_wrd + guess
        
        for guess_character in guess:
            if guess not in crt_wrd:
                tries = tries - 1
        from hangman_art import stages
        print(stages[tries])
        if tries <= 0:
            print("You lose")
            print("The word was: ", end=f"{crt_wrd}")
        if dsp_msg == crt_wrd:
            print("You Win!")
            break

    play_agn = input("Do you want to play again? (y/n) ")
    if play_agn == 'y':
        play_again = True
    else:
        play_again = False
        print('Thank you for playing.')
    from hangman_art import stages
    print(stages[tries])