# l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Standard Way
# l2 = []
# for i in range(1,101):
#     l2.append(i)
# print(l2)

# List Comprehension
# print([i for i in range(1,101)])

# Syntax : [append loop]

# Square=[]
# for i in range(1,101):
#    Square.append(i*i)
# print(Square)

# print([i*i for i in range(1,101)])

# Print numbers from -1 to -10 inside a list

# negative=[]
# u=-10
# for i in range(-10,0):
#     negative.insert(u,i)
#     print(f"{u}:{i}")
#     u+=1

# print(negative)

# print([-i for i in range(1,11)])

names = ["alan", "mark", "david"]

# l2 = ["al", "ma", "da"]
# letter2=[]
# for name in names:
#     letter2.append(name[0:2])
# print (letter2)
# print([name[0:2] for name in names])

numbers = [1,2,3,4,5,6,7,8,9,10]

# evens = []

# for number in numbers:
#     if number%2 == 0:
#         evens.append(number)

# print(evens)

# print([number for number in numbers if number%2 == 0])

output = []
# output -> [-1,4,-3,16,-5,36,-7,64,-9,100]

for number in numbers:
    if number%2!=0:
        output.append(-number)
    else:
        output.append(number*number)
    
print(output)

print([-i if i%2 != 0 else i*i for i in range(1,11)])

# [append from the if   if statement    else keyword    append from the else    for loop]
