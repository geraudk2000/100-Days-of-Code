from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# to solve end of list of alphabet, duplicate the alphabet

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print(logo)

def caesar(direction, text, shift):
    caesar_text = ""
    if direction == "decode":
        shift *= -1 
    for letter in text:
        position = alphabet.index(letter)
        caesar_text += alphabet[position+shift]
    print(f"your {direction} message is --> " + caesar_text)
 
    return caesar_text

caesar(direction, text, shift)