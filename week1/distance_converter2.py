
# Input metres
feet = float(input("Enter the number of feet: "))
inches = float(input("Enter the number of inches: "))

wholeInches = (feet * 12) + inches

centimetres = wholeInches * 2.54

metres = centimetres / 100

# Print whole_feet, inches
print(f"The distance in metres is {metres:.4f} metres")

