from random import randint

play_again = True
attmpt_cntr =10
rerun= False
print("Welcome to the number guessing game!! ")
print(" Guess a number between 1 & 100 ")
difficulty = input(" please choose a difficulty: EASY / HARD: ")

if difficulty==("hard"):
    attmpt_cntr =  attmpt_cntr-5
else:
    attmpt_cntr =  10

print(f"you have {attmpt_cntr} guess's ")
while play_again: 
    win = False
    crt_num = randint(1,100)
    atmpt_count = 0 
    while not win:
        attmpt_cntr = attmpt_cntr-1
        atmpt_count= atmpt_count+1
        number = int(input("Guess a number: ")) 
        # if rerun==True:
        #     print(" Guess a number between 1 & 100 ")
        #     difficulty = input(" please choose a difficulty: EASY / HARD: ") 
        if number==crt_num:
            print("spot on!")
            print(f"you've guessed {atmpt_count} times")
            win = True
            re_run = input("would you like to play again?:")
            if re_run== "yes":
                rerun = True
                play_again = True
            else:
                play_again = False
        elif attmpt_cntr==0:
            print("you've run out of guess's")
            rerun = input("would you like to play again?:")
            win = True
            if rerun== "yes":
                play_again = True
            else:
                play_again = False
        elif number<crt_num:
                print("It's Higher than that! Guess again")
                print(f"you have {attmpt_cntr} guess's left ")     
        elif number>crt_num:
            print("It's Lower than that! Guess again")
            print(f"you have {attmpt_cntr} guess's left ")
print("Thank you for playing!!")
        