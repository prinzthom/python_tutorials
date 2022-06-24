alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

options=input("enter 'encode' to encrypt OR 'decode' to decrypt: ")

message=input("type your message in: ")
shift=int(input("type the shift number in: "))

txt_len=((len(message))-1)
cyphr_txt=[]
encrypted_txt=[]
shift_val=shift
i=0
u=0
while i<=txt_len:
    for letter in message:
        letr=letter
        cyphr_txt.insert(i,letr)
        i=i+1
        for x in cyphr_txt:
            while u<=txt_len:
                if x in alphabet:
                    y=x+(shift_val)
                    encrypted_txt.append(u,y)
                    u=u+1
print(encrypted_txt[0::1])

# length=len(message)
# print(length)
# if options==("encode"):
#     for lttrs in message:
#         posisiton=




# def freq_check(freq):
#     for x in freq:
#         if x not in uniq_freq:
#             uniq_freq.append(x)

#     for x in uniq_freq:
#         print (x)
