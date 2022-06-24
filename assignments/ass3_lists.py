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

# name_cnt=0

# print(name)
# name_letter_count=[]
# name=names[0]


def freq_check(freq):
    for x in freq:
        if x not in uniq_freq:
            uniq_freq.append(x)

    for x in uniq_freq:
        print (x)
u=0
i=0
j=0
nameslenght=len(names)



while u<=nameslenght:
    for name in names:
        namelenght=len(name)   
        while j<=namelenght:
            freq=[]
            uniq_freq=[]
            print(f"{name} word count:")
            for letters in name:
                letter=letters
                # print(letter,name.count(letter))
                y=(letter) + ':' + str(name.count(letter))
                # print (y)
                freq.insert(i,y)
                i=i+1
                j+=1
                freq_check(freq)
u+=1
        

# freq_check(freq)  
# print(uniq_freq)
# print(name_letter_count)
# print(f"{name} word count:")
# freq.append[letter]
        # print(freq)
        # name_letter_count.append(freq)
    # name_cnt+=1
    # name_letter_count=[]


