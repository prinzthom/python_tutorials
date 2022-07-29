from multiprocessing.sharedctypes import Value


def addition(a,b):
    Value=0
    Value=(a+b)
    return Value
def subtraction(a,b):
    Value=0
    Value=(a-b)
    return Value
def multiply(a,b):
    Value=0
    Value=(a*b)
    return Value
def divide(a,b):
    Value=0
    Value=(a/b)
    return Value
    
methods = {
  "+": addition,
  "-": subtraction,
  "*": multiply,
  "/": divide
}

def calculator():

    use_again=True
    first_number=int(input("What's the first value: "))
    while use_again:
        for mthds in methods:
            print (mthds)
        method_slct=input("pick a operation: ")
        second_number=int(input("what's the second value: "))
        calc_mthd=methods[method_slct]
        output=calc_mthd(first_number, second_number)

        print(f"{first_number} {method_slct} {second_number} = {output}")

        use_agn=input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
        if use_agn == ('n'):
            use_again=False
            print("-----END-----")
            calculator()
        elif use_agn == ('y'):
            first_number=output
        else:
            use_again=False
calculator()


