# args is a way to create flexible functions

def add_nums(*args):
    total = 0
    for arg in args:
        total += arg
    return total

numbers = list(range(1,101))

print(add_nums(*numbers))
