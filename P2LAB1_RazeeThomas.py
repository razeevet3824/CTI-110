"""
Pseudocode:
BEGIN
    Ask for radius of the circle
    Calculate for Diameter
        2(radius)
    Calculate for Circumference
        2(pi)radius
    Calculate for Area
        PI r^2
    Display Diameter, Circumference, and Area
END
"""

# Thomas Razee
# March 2nd, 2026
# P1HW2
# Calculating Circle formulas and displaying results


radius = int(input("What is the radius of the circle? "))
print()
print("The Diameter of the circle is", 2 * radius)
print()
print("The Circumference of the circle is", 2 * 3.14 * radius)
print()
print("The Area of the circle is", 3.14 * radius**2)