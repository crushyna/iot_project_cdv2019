import pyodbc

server = 'sqlserveracs.database.windows.net'
database = 'AccessControl'
username = 'adminkamil'
password = 'CDVprojekt2019!'

driver = '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
row = cursor.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()