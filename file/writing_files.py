
'''
employee_file = open("file/employees.txt", "a")
print(employee_file.write("\nFile is Edited by Rixz_nv_1999"))
print(employee_file.write("\nCreated New Line"))
employee_file.close() '''
'''
employee_file = open("file/employees1.txt", "w")
print(employee_file.write("<p> <b> This File is Auto Created by script </b> </p>"))
print(employee_file.write("\n<p> <b> Cake is a cake even its a pancake </b> </p>"))
employee_file.close() '''

employee_file = open("file/ex.html", "w")
print(employee_file.write("<b><h1> This is a heading in HTML file </b> <h1>"))
print(employee_file.write("\n<b><i><u><h2> This is a heading in HTML file </b></i></u><h2>"))