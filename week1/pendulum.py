"""
 Calculate pendulum: 2 * pi * square(length/gravity)
"""

from math import pi,sqrt

GRAVITY = 9.81

lenthOfpendulum = float(input("Enter the length of the pendulum:"))

pendulum = 2 * pi * sqrt(lenthOfpendulum/ GRAVITY)

print(f"Period of the pendulum is {pendulum:.2f} seconds")