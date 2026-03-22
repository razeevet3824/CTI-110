"""
Pseudocode:
BEGIN
    Enter grades for modules 1-6
    Store modules in list named grades
    Blank line
    Display Result with -
    Calculate lowest grade:
        min(grades), :.1f
    Calculate highest grade:
        min(grades), :.1f
    Calculate sum of grades:
        min(grades), :.1f
    Calculate average:
        sum(grades) / len(grades), :.2f
    Display output of Lowest, Highest, Sum, and Average
    Have formatting in display, such as decimals and spacing necessary
    display '-'
END
"""

# Thomas Razee
# March 22, 2026
# P3LAB
# This program allows the user to enter a money (float) value with two places after the decimal. It then puts out the amount.

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