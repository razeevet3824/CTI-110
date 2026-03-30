"""
Pseudocode:
BEGIN
    1. Ask user to enter a grade for each prompted module
    2. Store the grades in a list of grades containing modules
    3. Calculate low, high, sum, and avg
    4.Display results with formatting
    5. Determine letter grade:
      90-100 = A
      80-89 = B
      70-79 = C
      60-69 = D
      <60 = F
END
"""

# Thomas Razee
# March 29, 2026
# P3HW1 - Debugging
# This program takes a number grade , determines average and displays letter grade for average.

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total/len(grades)

print("------------Results------------")
print(f'{"Lowest Grade":<19} {low:.1f}')
print(f'{"Highest Grade":<19} {high:.1f}')
print(f'{"Sum of Grades":<19} {total:.1f}')
print(f'{"Average":<19} {avg:.2f}')
print("---------------------------------------")
if avg >= 90:
 print('Your grade is: A')
elif avg >= 80: 
 print('Your grade is: B')
elif avg >= 70:
 print('Your grade is: C')
elif avg >= 60:
 print('Your grade is: D')
else:
 print('Your grade is: F')






