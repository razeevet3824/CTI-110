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
    Add Formatting for display output
END
"""

# Thomas Razee
# March 15, 2026
# P2HW1
# Adding formatting to display output of Travel expenses calculator


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
print(f'{"Location:":<19} {travel_destination}')
print(f'{"Initial Budget:":<19} ${budget:.2f}')
print(f'{"Fuel:":<19} ${gas:.2f}')
print(f'{"Accomodation:":<19} ${aprox_accomhotel:.2f}')
print(f'{"Food:":<19} ${food:.2f}')
print("---------------------------------------")
print()
print(f'{"Remaining Balance:":<19} ${budget - gas - aprox_accomhotel - food:.2f}')