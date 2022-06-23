win = 5
print("Hey! I'm thinking of a number between 1 to 10! Can you help me out?")

number = int(input("Guess a number: "))

if number==win:
    print("spot on!")
elif number>win:
    print("It's High!")
else:
    print("It's Low!")