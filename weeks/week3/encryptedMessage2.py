from string import ascii_lowercase, ascii_uppercase

def substitution(letter, factor):
    index = ascii_lowercase.find(letter)
    if(index + factor > 25):
        return ascii_uppercase[ (26 - factor) % index]; 

    return ascii_uppercase[index + factor]


originalMessage = input("Enter the message: ").lower()
message = ""
for character in originalMessage:
    if(not character.isalpha()):
        message += character
    else:
        index = ascii_lowercase.find(character)
        message += substitution(character, 3)

print(f"The enciphered message is: {message}")

