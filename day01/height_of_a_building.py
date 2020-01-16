# Program to calculate the height of the tree/building

import math

# Input

dist = float(input('Enter distance from the building in mts: '))
theta = float(input('Angle of sight in degrees: '))


# Process

theta_in_radians = math.radians(theta)
height = dist * math.tan(theta_in_radians)

# Output

print('Height of the building is %.2f mts' % height)
