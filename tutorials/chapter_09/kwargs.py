def func(**kwargs):
    fullname = ""
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")
        fullname += kwargs[key] + " "

    print(f"Hey! Your full name is {fullname}")

# func(name = "kaustubh", age = 65, email = "kaustubhkalpeshwankhede@outlook.com", city = "Nashik", state = "Maharashtra")
func(firstname = input("Insert your firstname: "), lastname = input("Insert your lastname: "))