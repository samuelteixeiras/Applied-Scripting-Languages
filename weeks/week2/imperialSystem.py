
"""
A Hogshead is a measurement of volume in the Imperial system, equivalent to 2 barrels.

A barrel is equivalent to 36 gallons.

A gallon is equivalent to 4.54609 litres.

Receives as input the number of hogsheads and converts and displays the equivalent volume in litres.
"""

hogsheads = int(input("Enter the volume in Hogsheads: "))

def hogsheadsToBarrel(hogsheads):
    return hogsheads * 2

def barrelToGallon(barrel):
    return barrel * 36

def gallonsToLitres(gallon):
    return float(gallon) * 4.54609

barrels =  hogsheadsToBarrel(hogsheads)

gallons = barrelToGallon(barrels)

litres = gallonsToLitres(gallons)


print(f"Equivalent volume in litres is {litres:.1f}")

