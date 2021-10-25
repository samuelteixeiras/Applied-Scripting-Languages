
nameSecret = "aladdin"
passwordSecret = "open_sesame"
name = input("Username: ")
password = input("Password: ")

numberOfTries = 0
loginFailed = False

while name != nameSecret or password != passwordSecret:
    print("Incorrect username or password")
    
    numberOfTries +=1 
    if(numberOfTries >= 3):
        loginFailed = True
        print("Login failed")
        break

    name = input("Username: ")
    password = input("Password: ")

if(not loginFailed):
    print("Login successful")




