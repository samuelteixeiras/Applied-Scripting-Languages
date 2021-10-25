
nameSecret = "aladdin"
passwordSecret = "open_sesame"
name = input("Username: ")
password = input("Password: ")



while name != nameSecret or password != passwordSecret:
    print("Incorrect username or password")
    name = input("Username: ")
    password = input("Password: ")

print("Login successful")




