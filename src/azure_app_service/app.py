from flask import Flask
import pyodbc
import pypyodbc

server = 'sqlserveracs.database.windows.net'
database = 'AccessControl'
username = 'adminkamil'
password = 'CDVprojekt2019!'
driver = '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect(
    'DRIVER={0};SERVER={1};PORT=1433;DATABASE={2};UID={3};PWD={4};'.format(driver, server, database, username, password))

cursor = cnxn.cursor()

app = Flask(__name__)


@app.route('/')
def WelcomePage():
    return '''Hello, World!
			This is our Access Control IoT project for CDV.
			Made by:
			Kamil Gruszczynski | 
			Radek Malinowski
			'''


@app.route('/database')
def data():
    """
    query_string = '''SELECT * FROM [dbo].[Persons]'''
    query_list = []
    cursor.execute(query_string)
    row = cursor.fetchone()
    while row:
        for each_row in row:
            query_list.append(each_row)
            print(each_row)

        row = cursor.fetchone()

    return query_list
    """
    cursor.execute("SELECT * FROM Persons")
    row = cursor.fetchone()
    fetch = row
    # fetch = (str(row[0]) + " " +str(row[1]))
    # row = cursor.fetchone()
    return fetch