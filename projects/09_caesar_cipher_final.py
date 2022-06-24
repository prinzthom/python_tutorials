alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(start_text, shift_number):
    encoded_message = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = position + shift_number
            encoded_message += alphabet[new_pos]
        else:
            encoded_message += char
    print(encoded_message)

def decode(start_text, shift_number):
    decoded_message = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = position - shift_number
            decoded_message += alphabet[new_pos]
        else:
            decoded_message += char
    print(decoded_message)

options=input("enter 'encode' to encrypt OR 'decode' to decrypt: ")
message=input("type your message in: ")
shift=int(input("type the shift number in: "))

if options == "encode":
    encode(message, shift)
else:
    decode(message, shift)