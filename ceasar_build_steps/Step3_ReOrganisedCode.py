alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def ceasar(text, shift):
  result = ""
  for letter in text:
    if letter in alphabet:
        position = alphabet.index(letter)
        if direction == "encode":
          new_position = (position + shift) % 26
        elif direction == "decode":
          new_position = (position - shift) % 26
        else:
          print("Invalid input")
          return
    result += alphabet[new_position]
  else:
    text += letter
  print(f"The {direction}d text is {result}")
ceasar(text, shift)


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

#Method 2 
"""
But this has an issue that is anything apart from 'decode' would recognised as encode

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
"""
