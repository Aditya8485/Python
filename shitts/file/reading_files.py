
'''
with open("file/employees.txt", "r") as data_file:
    for data in data_file.readlines():
        print(data)
'''


with open("file/employees.txt", "r") as data:
    for data in data.readlines():
        print(data)


employee_file = open("file/employees.txt", "r")
print(employee_file.read())
print(employee_file.readline())
print(employee_file.seek(0))

employee_file.close()
