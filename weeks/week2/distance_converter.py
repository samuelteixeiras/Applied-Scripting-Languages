
# Input metres
metres = float(input("Enter the distance in metres: "))

# Calculate feet as metres x 3.28084 
feet = metres * 3.28084 

# Calculate whole_feet as integer part of feet
whole_feet = int(feet)

# Calculate inches as (feet - whole_feet) * 12
inches = (feet - whole_feet) * 12

# Print whole_feet, inches
print(f"Equivalent distance is {whole_feet} feet, {inches:.2f} inches")

