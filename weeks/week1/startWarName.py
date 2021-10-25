
firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")
maiden = input("Enter your mother's maiden name: ")
placeOfBirth = input("Enter the name of your birthplace: ")


startWarsFirstName = (firstname[:3] + lastname[:2]).title()
startWarsLastName = (maiden[:2] + placeOfBirth[:3]).title()

print("Your Star Wars name is:", startWarsFirstName, startWarsLastName)


"""
For your Star Wars first name:
Take the first 3 letters of your first name
add the first 2 letters of your last name
For your Star Wars last name:
Take the first 2 letters of your Mother's maiden name
add the first 3 letters of the place you were born
Display the name with appropriate capitalisation.
"""