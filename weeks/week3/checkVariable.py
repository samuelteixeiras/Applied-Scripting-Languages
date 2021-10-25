# Input firstname
name = input("Enter the variable name: ")

chars = list(name)
invalid = ""

for i in range(len(chars)):
    if not chars[i].isnumeric() and not chars[i].isalnum() and chars[i] != "_":
        invalid = chars[i]
        break


if invalid != "":
    print(f"Invalid character {invalid}") 
else:
    print("Valid variable name")     


