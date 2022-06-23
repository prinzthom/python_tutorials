from itertools import count


names = ["kaustubh", "prince"]

"""
Kaustubh Word Count:
k : 1
a : 1
u : 2
s : 1
t : 1
b : 1
h : 1

Prince Word Count:
.
.
.
.
.
"""
name=names[0]
namelenght=len(name)
print(name)

print(f"{name} word count:")

for letter in name:
    print(f"{letter}:{name.count(letter)}")
    output=(f"{letter}{name.count(letter)}")
    lttr_count=[]
    lttr_count.extend([output])
    if name.count(letter)==2:
        lttr_count.sort
for position in range(namelenght):
    letter = name[position]

    print(f" {position}:{letter}:{name.count(letter)} ")


