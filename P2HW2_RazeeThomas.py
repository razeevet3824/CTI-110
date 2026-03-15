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
# March 15, 2026
# P2HW2
# Design program to track grades from each module using input, and use to list grading in output

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))
grades = [module1, module2, module3, module4, module5, module6]
print()
print("------------Results------------")
print(f'{"Lowest Grade:":<19} {min(grades):.1f}')
print(f'{"Highest Grade:":<19} {max(grades):.1f}')
print(f'{"Sum of Grades:":<19} {sum(grades):.1f}')
print(f'{"Average:":<19} {sum(grades) / len(grades):.2f}')
print('-' * 40)