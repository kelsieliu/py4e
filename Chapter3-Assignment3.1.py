3.1 Write a program to prompt the user for hours and rate per hour using input to
compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the
hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50
per hour to test the program (the pay should be 498.75). You should use input to
read a string and float() to convert the string to a number. Do not worry about error
checking the user input - assume the user types numbers properly.

Desired Output
498.75

Code:
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

if h <= 40:
    cgp = h * r 
    print(cgp)
elif h > 40:
    cgp = 40 * r + (h-40)*r*1.5
    print(cgp)

Your Output
498.75