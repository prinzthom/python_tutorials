def table(num):
    i=0
    u=num
    j=0
    while i<10:
        i=i+1
        j=num*i
        print(f"{num}x{i}={j}")

number = int(input("Insert a number: "))

table(number)

"""
3x1 = 3
3x2 = 6
3x3 = 9
.
.
.
.
.
.
.
3x10 = 30
"""