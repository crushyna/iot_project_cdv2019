import pyodbc

server = 'sqlserveracs.database.windows.net'
database = 'AccessControl'
username = 'adminkamil'
password = 'CDVprojekt2019!'

driver = '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT TOP (10) * FROM [dbo].[Persons]")
row = cursor.fetchone()
while row:
    # print(str(row[0]) + " " + str(row[1]))
    for each_row in row:
        print(each_row)

    row = cursor.fetchone()