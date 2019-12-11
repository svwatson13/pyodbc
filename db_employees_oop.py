from db_connect_oop import *
import time
class NWEmployees(MSDBConnection):
    def print_all(self):
        query = 'SELECT * FROM Employees'
        data = self.sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"ID: {record.EmployeeID} - {record.TitleOfCourtesy} {record.FirstName} {record.LastName}")

    def read_one_ID(self):
        ID = (int(input('select an ID ')))
        query = f'SELECT * FROM Employees WHERE EmployeeID like ({ID})'
        data = self.sql_query(query)
        record = data.fetchone()
        print('getting employee')
        time.sleep(1)
        print(f"ID: {record.EmployeeID} - {record.TitleOfCourtesy} {record.FirstName} {record.LastName}")

    def read_one_name(self):
        name = input('What is the name? ')
        query = f"SELECT * FROM Employees WHERE FirstName like '{name}' or LastName like '{name}'"
        data = self.sql_query(query)
        record = data.fetchone()
        print('getting employee')
        time.sleep(1)
        print(f"ID: {record.EmployeeID} - {record.TitleOfCourtesy} {record.FirstName} {record.LastName}")

    def add_employee(self):
        title = input('What is their title? ')
        first_name = input('What is the first name of this employee ').strip()
        last_name = input('What is the last name of this employee ').strip()
        query = f"INSERT into Employees (TitleOfCourtesy, FirstName, LastName) values ('{title}', '{first_name}', '{last_name}')"
        query1 = 'SELECT * FROM Employees'
        data = super().sql_query(query)
        data1 = self.sql_query(query1)
        while True:
            record = data1.fetchone()
            if record is None:
                break
            print(f"ID: {record.EmployeeID} - {record.TitleOfCourtesy} {record.FirstName} {record.LastName}")

    def change_employee(self):
        user_input = input('What column do you wish to change? ')
        user_change = input('What do you want to change this to? ')
        employee_info = input('Whats the employees ID? ').strip()
        query = f"UPDATE TABLE Employees SET {user_input} = {user_change} where EmployeeID like {employee_info} "
        data = super().sql_query(query)
