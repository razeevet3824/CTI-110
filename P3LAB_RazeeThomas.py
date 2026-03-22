"""
Pseudocode:
BEGIN
    Question user amount of money of their choice to see as a float
    configure change
     int(amount * 100)
    calculation for dollars, quarters, dimes, nickels, and pennies change
    change // value of that change
    change = change - (change type * value of that change)
    if the value is none, display "No change", showing of no value
    if is value, display the visible types of change amount that is necessary to create that input from user
END
"""

# Thomas Razee
# March 22, 2026
# P3LAB
# This program allows the user to enter a money (float) value with two places after the decimal. It then puts out the changes needed.

amount = float(input("Enter the amount of money as a float: $"))
change = int(amount * 100)

dollars = change // 100
change = change - (dollars * 100)
quarters = change // 25
change = change - (quarters * 25)
dimes = change // 10
change = change - (dimes * 10)
nickels = change // 5
change = change - (nickels * 5)
pennies = change

if change == 0:
    print("No change")
if dollars > 0:
    if dollars == 1:
        print(f"{dollars} Dollar")
    else:
        print(f"{dollars} Dollars")
if quarters > 0:
    if quarters == 1:
        print(f"{quarters} Quarter")
    else:
        print(f"{quarters} Quarters")
if dimes > 0:
    if dimes == 1:
        print(f"{dimes} Dime")
    else:
        print(f"{dimes} Dimes")
if nickels > 0:
    if nickels == 1:
        print(f"{nickels} Nickel")
    else:
        print(f"{nickels} Nickels")
if pennies > 0:
    if pennies == 1:
        print(f"{pennies} Penny")
    else:
        print(f"{pennies} Pennies")