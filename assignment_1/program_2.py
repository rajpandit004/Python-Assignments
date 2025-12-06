# The Temperature of a city in Fahrenheit degrees is input through the keyboard.
# Write a program to convert this temperature into Centigrade degrees.

fahrenheit = float(input("Enter temperature in fahrenheit: "))

# Convert fahrenheit into celsius
celsius = (fahrenheit - 32) * 5 / 9

print("The temperature in celsius:", celsius)
