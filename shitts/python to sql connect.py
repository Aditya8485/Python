"""Python MySql create Table"""

'''To create table use CREATE TABLE table_name (column1 datatype, column2 datatype, column3 datatype, ....);'''

"""Create a table named "customers" """

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",  #Your host name, usually localhost
    user = "yourusername",       #Your MySQL username, usually root
    password = "yourpassword"    #Your MySQL password, if you have set one
    database = "mydatabase"

)

mycursor = mydb.cursor(
    "Create table customers (" \
    "Create VARCHAR(255) , " \
    "adress VARCHAR(255))")



)
