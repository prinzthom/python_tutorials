print ("welcome to treasure island")

ch_1=input ("would you like to go LEFT or RIGHT: ")

if ch_1==("left"):

    CH_2 = input ("you walk for a while and arrive to a rivver would you like to WAIT for a ferrymen or SWIM across: ")

    if CH_2==("wait"):

        ch_3 = input("you take a ferry and arrive across, you find a house with three doors: a RED, BLUE and YELLOW one which do you chose to enter first: ")

        if ch_3==("yellow"):
            print ("you've found the treasure trove! you've won the game")

        elif ch_3==("red"):
            print ("you opend a room full of fire , you were burnt to death")

        else:
            print ("you walked into a den of beasts")

    else :
        print ("you were washed away by the rapid tides and drowned")
        print ("you died")

else:
    print ("you triped and fell into a pit of snakes")
    print ("you died")
