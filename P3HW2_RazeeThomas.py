"""
Pseudocode:
BEGIN
    1. Ask for Employee's name
    2. Ask for # of hours worked
    3. Ask for pay rate, evalulate if overtime, and if so, calculate amount owed for overtime and make them receive 1.5s their normal pay rate for #s worked overtime.
    4. Calculate pay for regular hours
    5. Display gross pay
    6. Display following: Employee name, pay rate, number of hours worked, overtime hours, pay for regular hours, and gross pay)
END
"""

# Thomas Razee
# March 29, 2026
# P3HW2
# A program that asks for information about an employee and can display calculations and information about said employee

emp_name = input("Enter employee's name: ")
emp_hours = float(input("Enter number of hours worked: "))
emp_rate = float(input("Enter employee's pay rate: "))
if emp_hours > 40:
    ot_hours = emp_hours - 40
    ot_pay = ot_hours * (emp_rate * 1.5)
    reg_pay = 40 * emp_rate
else:
    ot_hours = 0
    ot_pay = 0
    reg_pay = emp_hours * emp_rate
gross_pay = reg_pay + ot_pay
print("------------------------------------------")
print(f'{"Employee name:":<15} {emp_name}')

print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("------------------------------------------------------------------------------------------")
print(f'{emp_hours:<16.1f}{emp_rate:<12.1f}{ot_hours:<12.1f}{ot_pay:<16.2f}${reg_pay:<14.2f}${gross_pay:.2f}')