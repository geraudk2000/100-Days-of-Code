from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# to solve end of list of alphabet, duplicate the alphabet

print(logo)
continue_game = True

def caesar(direction, text, shift):
    caesar_text = ""
    if direction == "decode":
        shift *= -1 
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            caesar_text += alphabet[position+shift]
        else:
            caesar_text += char
    print(f"your {direction} message is --> " + caesar_text)
    
    return caesar_text

while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26
    caesar(direction, text, shift)
    
    again = input("Do you want to continue? pres yes or any keys to exit ").lower()

    if again != 'yes':
        print("Goodbye!!")
        continue_game = False