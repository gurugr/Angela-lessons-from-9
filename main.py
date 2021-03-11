
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ',',', '.', '=','-', '@', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0','+']
print(len(alphabet))

def caeser(plan_text,shift_amount,ciper_direction):
  
  cipher_letter = ""
  if ciper_direction == "decode":
    shift_amount *= -1
  for char in plan_text:
    if char not in alphabet:
      cipher_letter += char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      new_position = (new_position % len(alphabet))
      cipher_letter += alphabet[new_position]

  print(f"The {ciper_direction}d text is {cipher_letter}")

while True:
  continue_game = input("Do you wan to continue the game 'yes' or 'no' ?\n")
  if continue_game == "yes".lower():
  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    # shift = shift % 44
    caeser(plan_text=text,shift_amount=shift,ciper_direction=direction)
       
  else:
    print("Good Bye")
  