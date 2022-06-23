# def add_two(a,b):
#     print(a+b)

# add_two(1,2)

# def greater(a,b):
#     if a>b:
#         return a 
#     else:
#         return b
# print(greater(8,4))


def greatest(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif a<b and b>c and b>d:
        return b
    elif c>a and c>b and c>d:
        return c
    else:
        return d

print(greatest(3,45,76,8))