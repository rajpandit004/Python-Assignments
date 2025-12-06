# Ramesh’s basic salary is input through the keyboard.
# His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary.
# Write a program to calculate his gross salary.

salary = int(input("Enter your salary: "))

# Calculate the allowances
allowance1 = (salary * 40) / 100
allowance2 = (salary * 20) / 100

# Calculate the gross salary
gross_salary = salary + allowance1 + allowance2

print("The gross salary is", gross_salary)
