def paldrm_chk(word):
    rev = word[-1::-1] 
    if word == rev:
        print ("this word is a palindrome")
        print(f"{rev}")
    else:
        print("this word is not a palindrome")


name = input("type in a word: ")
paldrm_chk(name)
