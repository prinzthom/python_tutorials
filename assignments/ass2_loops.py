# Sum up the numbers from 1 to 10 with loops ( The output should be 55 )
# u=1
# i=2
# j=0
# while j<46:
#     j=i+u
#     print (f"{u}+{i}={j}")
#     u=i+u
#     i=i+1

# 1+2+3+4+5+6+7+8+9+10 = 55

# print("Hello!", end=" + ")
# print("Hey!")

total = 0
i = 1
while i <= 10:
    print(i, end = " + ")
    total += i
    i += 1
print(total)