# Functions which enhances the functionality of other functions

def decorator_func(prince):
    def wrapper(*args, **kwargs):
        print("Hey! This is from the dec")
        return prince(*args, **kwargs)
    return wrapper

def func1():
    print("Hey! I am Function1")

@decorator_func
def add_two(a,b):
    print(a+b)

@decorator_func
def add_two2(a,b):
    return a+b

add_two(1,2)
print(add_two2(3,4))