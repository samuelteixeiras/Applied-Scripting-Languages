# Input firstname
name = input("Enter your first and last names, separated by a space: ")

names = name.lower().split(" ")
firstName = names[0]
lastName = names[1]
username = firstName.lower() + lastName[0]

print("Your username is: ", username)
