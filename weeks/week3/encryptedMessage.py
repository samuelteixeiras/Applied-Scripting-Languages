from string import ascii_lowercase


originalMessage = input("Enter a message to encipher: ").lower()
message = ""
for character in originalMessage:
    if(not character.isalpha()):
        message += character
    else:
        index = ascii_lowercase.find(character)
        message += ascii_lowercase[25 - index]

print(f"Encrypted message is: {message}")