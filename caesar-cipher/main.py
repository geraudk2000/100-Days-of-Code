from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# to solve end of list of alphabet, duplicate the alphabet

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  

#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

def caesar(direction, text, shift):
  caesar_text = ""
  if direction == "encode":
    for letter in text:
      position = alphabet.index(letter)
      caesar_text += alphabet[position+shift]
    print(f"Your {direction} message is --> " + caesar_text)
  elif direction == "decode":
    for letter in text:
      position = alphabet.index(letter)
      caesar_text += alphabet[position-shift]
    print(f"Your {direction} message is --> " + caesar_text)
  else:
    print("Wrong option, try again.")
  return caesar_text
  
  

    
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
caesar(direction, text, shift)

