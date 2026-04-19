import csv


with open('../csv/employees.csv', 'r')as file:
    reader = csv.reader(file)
    employees = [row for row in reader]

employee_names = [' '.join(i[1:3]) for i in employees[1:]]

print(employee_names)

names_with_e = [name for name in employee_names if 'e' in name]

print(names_with_e)