age = int(input("What's your age: "))

if age >= 18 and age <= 100:
    print("You are eligible for voting.")
elif age > 100 or age < 1:
    print("You are probably from some other planet!")
else:
    print("You are not eligible for voting.")
