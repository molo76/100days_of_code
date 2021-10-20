import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keep_going = "yes"

def caesar(input, shift_amount, command):
  output_text = ""
  if shift_amount >= 26:
    shift_amount %= 26
  if command == "decode":
    shift_amount *= -1
  for char in input:
    if char not in alphabet:
      output_text += char
    else:
      if alphabet.index(char) + shift_amount >= 26:
        output_text += alphabet[alphabet.index(char) + shift_amount -26]
      elif alphabet.index(char) + shift_amount < 0:
        output_text += alphabet[alphabet.index(char) + shift_amount +26]
      else: 
        output_text += alphabet[alphabet.index(char) + shift_amount]
  print(f"Your {direction}d text is: {output_text}")

while keep_going == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  keep_going = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
  if keep_going == "no":
    print("Goodbye!")