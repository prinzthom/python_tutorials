try:
    age = int(input("Insert your age: "))

    if age >= 18 and age <= 116:
        print("You are eligible for voting!")
    elif age > 116 or age < 1:
        print("Maybe, you are trying to fool us!")
    else:
        print("You are not eligible for voting.")
except Exception as err:
    print(err)

