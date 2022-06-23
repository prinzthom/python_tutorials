names=["prince","noel","richard","dave"]
name_in= input("enter your name: ")

# In, Not In
if name_in in names:
    print(f"{name_in} exists")
else:
    print(f"{name_in} doesn't exist")