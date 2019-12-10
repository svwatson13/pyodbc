import pyodbc

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = docker_Northwind.cursor()

cursor.execute("SELECT * FROM Customers WHERE city LIKE 'London'")

# Fetching data from the executed SQL command and printing
row = cursor.fetchone()
print(row)

# Cursor maintaining state
print(cursor.fetchone())
print(cursor.fetchone())

# Accesing specific data or column
## Use column name as attribute of the entry
row = cursor.fetchone()
print(row)
print(row.CompanyName, row.ContactName)

# Fetchall Method - bad
rows_all = cursor.fetchall()
print(rows_all)
print(type(rows_all))

for row in rows_all:
    print(row.ContactName, '-', row.CompanyName, '-', row.Fax)

# To get lots of data - use a while loop and fetchone at a time
rows = cursor.execute("SELECT * FROM Products")
while True:
    record = rows.fetchone()
    if record is None:
        break
    else:
        print(record.UnitPrice)
