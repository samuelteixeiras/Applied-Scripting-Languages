length = float(input("Enter the length in metre: "))
width = float(input("Enter the width in metres: "))

def area(length,width):
    return length * width
    
def perimeter(length,width):
    return 2 * (length + width)

print(f"The area is {area(length,width):.1f} square metres")    
print(f"The perimeter is {perimeter(length,width):.1f} metres")