import csv
import traceback

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

# # Task 8
# def employee_dict(row):
#     employee_info = {
#         f"{employees['fields'][1]}": f"{row[1]}",
#         f"{employees['fields'][2]}": f"{row[2]}",
#         f"{employees['fields'][3]}": f"{row[3]}"
#     }

#     return employee_info

# print(employee_dict(employees["rows"][8]))