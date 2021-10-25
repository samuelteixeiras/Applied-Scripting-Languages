# Input firstname
name = input("Enter your username: ")

if len(name) < 4:
    print("Username is invalid:\n	Too short - must have between 4 and 8 alphanumeric characters") 
elif len(name) > 8:
    print("Username is invalid:\n	Too long - must have between 4 and 8 alphanumeric characters") 
elif not name[0].islower():
    print("Username is invalid:\n	Does not start with a lowercase letter") 
elif not name.isalnum():
    print("Username is invalid:\n	Contains non-alphanumeric characters") 
else:
    print("Valid username")     


