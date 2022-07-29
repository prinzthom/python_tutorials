class Person:
    def __init__(self, firstname, lastname, age, email):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email

    def introduction(self):
        return f"Hey! I am {self.firstname} {self.lastname}. I am {self.age} years old. You can contact me at {self.email}"

p1 = Person("prince", "thomas", 21, "prince.thomas@gmail.com")

print(p1.introduction())

print(type(p1))
name = "ster"
print(type(name))
l1 = [123123,123,123,123]
print(type(l1))