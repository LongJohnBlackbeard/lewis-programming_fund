# Daniel Tujo
# CPSC 21000 002
# This program awatds graduation honors

gpa = float(input("Enter you gpa: "))
if gpa >=3.9:
    print("Highest Honors")
elif gpa >= 3.75:
    print("High Honors")
elif gpa >= 3.5:
    print("Honors")
else:
    print("No Honors")

temp = float(input('Enter temp: '))
tempf = (9/5 * temp) + 32
print(tempf)