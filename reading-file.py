
# Read file
employee_file = open("functions.py", "r")

print(employee_file.read())
employee_file.close()
# Read file line by line
employee_file = open("functions.py", "r")

print(employee_file.read())
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()

# Read file in list
employee_file = open("functions.py", "r")

print(employee_file.readlines())
employee_file.close()

# Read file in list and loop
employee_file = open("functions.py", "r")

for employee in employee_file.readlines():
    print(employee)
employee_file.close()