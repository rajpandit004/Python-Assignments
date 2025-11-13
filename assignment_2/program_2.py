# If the ages of Ram, Shyam and Ajay are input through the keyboard,
# write a program to determine the youngest of the three.

r_age = int(input("Enter Ram's age: "))
s_age = int(input("Enter Shyam's age: "))
a_age = int(input("Enter Ajay's age: "))

# Finding the youngest among three
if r_age < s_age:
    if r_age < a_age:
        print("Ram is youngest")
    else:
        print("Ajay is youngest")
else:
    if s_age < a_age:
        print("Shyam is youngest")
    else:
        print("Ajay is youngest")
