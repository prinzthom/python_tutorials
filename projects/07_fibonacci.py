def fibonacci(number):
    a=0
    b=1
    if number == 1:
        print(a)
    elif number == 2:
        print(a,b)
    else:
        print(a,b, end = " ")
        for _ in range(number-2):
            c = a+b
            a=b
            b=c
            print(c, end = " ")
   
number=int(input("enter the number of fibonacci numbers: "))
fibonacci(number)
