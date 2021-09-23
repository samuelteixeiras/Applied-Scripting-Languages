"""
 Calculate prolate spheroid 
"""

from math import pi,sqrt, asin

a = float(input("Enter semi-axis a: "))
b = float(input("Enter semi-axis b: "))


e = float(sqrt( (a ** 2) - (b ** 2)) / a)

part2 = (b + ( (a * asin(e)) / e) )

prolateSpheroid = 2 * pi * b * part2


print(f"The surface area is: {prolateSpheroid:.2f}")