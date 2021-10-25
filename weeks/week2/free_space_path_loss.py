# Program to calculate Free Space Path Loss
from math import pi, log10

# Input distance
distance = float(input('Enter the distance from the transmitter in metres '))

# Input frequency 
frequency = float(input('Enter the signal frequency in Hertz '))

# Calculate the free space path loss
fspl = (4 * pi * distance * frequency / 300000000) ** 2
# Print the free space path loss
print('The Free Space Path Loss is', round(fspl,3))

# Calculate the free space path loss in decibels
fspldb = 20 * log10(distance) + 20 * log10(frequency) - 147.55

# Print the free space path loss in decibels
print('The Free Space Path Loss in Decibels is', round(fspldb,3), 'db')

