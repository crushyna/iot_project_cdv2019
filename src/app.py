from flask import Flask
import pyodbc


server = 'sqlserveracs.database.windows.net'
database = 'AccessControl'
username = 'adminkamil'
password = 'CDVprojekt2019!'
driver = '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT:1433;DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Persons")
row = cursor.fetchone()


app = Flask(__name__)

@app.route('/')
def WelcomePage():
	return '''Hello, World!
			This is our Access Control IoT project for CDV.
			Made by:
			Kamil Gruszczynski | 
			Radek Molik
			'''


@app.route('/database')
def data():
	fetch = row
	# fetch = (str(row[0]) + " " +str(row[1]))
	# row = cursor.fetchone()
	return fetch



