#Python program to find the area of a triangle whose sidea are given.
import math

# Function to calculate the area of a triangle
def triangle_area(a, b, c):
    # Semi-perimeter
    s = (a + b + c) / 2
    # Area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Input the sides of the triangle
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

# Check if the sides form a valid triangle
if a + b > c and a + c > b and b + c > a:
    # Calculate and display the area
    area = triangle_area(a, b, c)
    print(f"The area of the triangle with sides {a}, {b}, and {c} is: {area}")
else:
    print("The given sides do not form a valid triangle.")
