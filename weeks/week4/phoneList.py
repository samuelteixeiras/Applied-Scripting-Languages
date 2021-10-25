contacts = ["087 1234567", "090 9876543", "090 6468000", "112"]
text = ""

def init():
    text = input("[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ")
    return text.lower()

def printList():
    print("Numbers in your contacts list")
    for i in range(len(contacts)):
        print(f"{i} : {contacts[i]}")
    print("")

def checkNumber():
    number = input("Enter the number: ")
    if number in contacts:
        print(f"Number {number} is in the list\n")
    else:
        print(f"Number {number} is not in the list\n")

def addNumber():
    number = input("Enter new number: ")
    contacts.append(number)
    print(f"Added {number} to the list\n")    

def editNumber():
    number = input("Enter number to edit: ")
    newNumber = input("Enter the new number: ")
    for i in range(len(contacts)):
        if contacts[i] == number:
            contacts[i] = newNumber
    print(f"Replaced {number} with {newNumber}\n")

def deleteNumber():
    number = input("Enter number to delete: ")
    if number in contacts:
        contacts.remove(number)
    print(f"Removed {number} from the list\n")    

while(text != "q"):
    text = init()

    if text == "p":
        printList()
    elif text == "c":
        checkNumber()
    elif text == "a":
        addNumber()
    elif text == "e":
        editNumber()
    elif text == "d":
        deleteNumber()
    elif text == "q":
        break
    else:
         break  

print("")



