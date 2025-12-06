# If the marks obtained by a student in five different subjects are input through the keyboard,
# find out the aggregate marks and percentage marks obtained by the student.
# Assume that the maximum marks that can be obtained by a student in each subject is 100.

s1 = int(input("Enter marks of 1st subject: "))
s2 = int(input("Enter marks of 2nd subject: "))
s3 = int(input("Enter marks of 3rd subject: "))
s4 = int(input("Enter marks of 4th subject: "))
s5 = int(input("Enter marks of 5th subject: "))

# Calculate aggregate marks
total = s1 + s2 + s3 + s4 + s5

# Calculate percentage
percentage = total / 5

print("Aggregate marks:", total)
print("Total percentage:", percentage)
