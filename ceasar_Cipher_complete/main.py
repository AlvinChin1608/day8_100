import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  for char in start_text:
      if char in alphabet:
          position = alphabet.index(char)
          if cipher_direction == "encode":
              new_position = (position + shift_amount) % 26
          elif cipher_direction == "decode":
              new_position = (position - shift_amount) % 26
          end_text += alphabet[new_position]
      else:
          end_text += char  # Keep the character as it is if not in the alphabet
  print(f"Here's the {cipher_direction}d result: {end_text}\n\n")

    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

#TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction not in ["encode","decode"]:
    print("Invalid Input")
    continue
  
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if restart != "yes":
    break
  #If the user types "yes", the loop continues from the beginning, asking for the direction, text, and shift again.