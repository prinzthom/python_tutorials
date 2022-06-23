from random import randint

play_again = True

print("Hey! I'm thinking of a number between 1 to 10! Can you help me out?")

while play_again:
    win = False
    atmpt_count = 0 
    crt_num = randint(1,10)

    while not win:
        atmpt_count= atmpt_count+1
        number = int(input("Guess a number: "))
        if number==crt_num:
            print("spot on!")
            print(f"you've guessed {atmpt_count} times")
            win = True
            rerun = input("would you like to play again?:")
            if rerun== "yes":
                play_again = True
            else:
                play_again = False
        elif number<crt_num:
                print("It's Higher than that! Guess again")
        else:
            print("It's Lower than that! Guess again")
        
