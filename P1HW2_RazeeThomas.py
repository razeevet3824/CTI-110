"""
Pseudocode:
BEGIN
    Display message about calculating travel expenses
    Ask user for their budget
    Ask user for travel destination
    Ask user for estimated gas cost
    Ask user for estimated accommodation/hotel cost
    Ask user for estimated food cost
    Calculate remaining balance as:
        budget - gas - accommodation - food
    Display travel expenses summary
    Display remaining balance
END
"""

# Thomas Razee
# February 28, 2026
# P1HW2
# Calculating travel expenses and of displaying travel information


print("This program calculates and displays travel expenses")
print()
budget = int(input("Enter Budget: "))
print()
travel_destination = (input("Enter your travel destination: "))
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
aprox_accomhotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()
print("------------Travel Expenses------------")
print("Location:", travel_destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", aprox_accomhotel)
print("Food:", food)
print()
print("Remaining Balance:", budget - gas - aprox_accomhotel - food)