import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task 2
def read_employees():
    employees_dict = {}
    employees_list = []

    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    employees_dict['fields'] = row
                else:
                    employees_list.append(row)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

    employees_dict['rows'] = employees_list

    return employees_dict

employees =  read_employees()

# print(employees)


# Task 3
def column_index(string):
    return employees["fields"].index(string)

employee_id_column = column_index('employee_id')


# Task 4
def first_name(row):
    first_name_column =  column_index('first_name')
    first_name = employees['rows'][row][first_name_column]
    return first_name


# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches


# Task 7
def sort_by_last_name():
    employees['rows'].sort(key=(lambda row: row[column_index('last_name')]))
    return employees['rows']

sort_by_last_name()

# print(employees['rows'])


# # Task 8
# def employee_dict(row):
#     employee_info = {
#         f"{employees['fields'][1]}": f"{row[1]}",
#         f"{employees['fields'][2]}": f"{row[2]}",
#         f"{employees['fields'][3]}": f"{row[3]}"
#     }

#     return employee_info

# print(employee_dict(employees["rows"][8]))

# Task 8
def employee_dict(row):
    employee_info = dict(zip(employees['fields'][1:], row[1:]))
    return employee_info

# print(employee_dict(employees["rows"][8]))

# Task 9
def all_employees_dict():
    all_employees = {}
    for employee in employees['rows']:
        all_employees[f'{employee[0]}'] = employee_dict(employee)
    return all_employees

# print(all_employees_dict())


# Task 10
def get_this_value():
    return os.getenv('THISVALUE')

# print(get_this_value())


# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    return 0

set_that_secret('Bingo!')
# print(custom_module.secret)

# Task 12
def read_minutes():
    
    notebooks = ['../csv/minutes1.csv', '../csv/minutes2.csv']

    def parse_notebook_data(notebook):
        with open(notebook, 'r') as file:
            reader = csv.reader(file)
            fields = next(reader)
            rows = [tuple(row) for row in reader]

        output ={
            'fields': fields,
            'rows': rows
            }
        return output
    
    parsed_data = [parse_notebook_data(x) for x in notebooks]

    return parsed_data

try:
    minutes1, minutes2 = read_minutes()
except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
# else:
#     print(minutes1, minutes2)

# Task 13
def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])

    combined_sets = set1.union(set2)

    return combined_sets

minutes_set = create_minutes_set()

# Task 14
def create_minutes_list():
    minutes_list = list(minutes_set)

    out = map((lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y"))), minutes_list)

    return list(out)

minutes_list = create_minutes_list()

# print(minutes_list)

# Task 15
def write_sorted_list():
    sorted_by_dt = sorted(minutes_list, key= lambda entry: entry[1])
    sorted_by_dt = map((lambda entry: (entry[0], datetime.strftime(entry[1], "%B %d, %Y"))), sorted_by_dt)
    sorted_by_dt = list(sorted_by_dt)

    with open('./minutes.csv', 'w', newline="")as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])
        writer.writerows(sorted_by_dt)
        # writer.writerows(minutes_list)
        
    return sorted_by_dt

sorted_list = write_sorted_list()
print(sorted_list)