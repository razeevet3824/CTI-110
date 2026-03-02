"""
Pseudocode:
BEGIN
    Create vehicles
    Create key to hold vehicles
    Create Vehicle choice
    Prompt to enter a vehicle to see mpg
    Display feedback
    Next prompt to amount of miles for vehicle
    display amount of gallons of gas and vehicle choice, along with miles
END
"""

# Thomas Razee
# March 2nd, 2026
# P2LAB2
# Create dictionary for vehicles containing key and value = name and number.


vehicle = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}
keys = vehicle.keys()
print(keys)
print()
vehchoice = input("Enter a vehicle to see it's mpg: ")
mpg = vehicle[vehchoice]
print()
print(f"\nThe", vehchoice, "gets", mpg, "mpg")
print()
miles = float(input(f"\nHow many miles will you drive the {vehchoice}? "))
galgas = miles / mpg
print(f"\n{galgas:.2f} gallon(s) of gas are needed to drive the {vehchoice} {miles:.1f} miles.")