import pyodbc
from db_products_oop import *
from db_connect_oop import *

class NWProducts(MSDBConnection):
    # Read all items from the Products table
    def read_all(self):
        query = 'SELECT * FROM Products'
        data = super().sql_query(query)
        return data

    # Set ID for items in Products
    def set_id(self):
        ID = int(input('select an ID'))
        return ID

    def read_one_ID(self):
        ID = (int(input('select an ID ')))
        query = f'SELECT * FROM Products WHERE ProductID like ({ID})'
        info = super().sql_query(query)
        return info

    def read_one_product_name(self):
        Product_Name = input('select a name ').strip()
        query = f"SELECT * FROM Products WHERE ProductName like '{Product_Name}'"
        info = super().sql_query(query)
        return info

    def print_all(self):
        query = 'SELECT * FROM Products'
        data = self.sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            else:
                print(f"ID: {record.ProductID} - {record.ProductName} - £{record.UnitPrice}")

    def top_10_price(self):
        a = 0
        query = 'SELECT top 10 * FROM Products ORDER BY UnitPrice desc'
        data = self.sql_query(query)
        while True:
            a += 1
            record = data.fetchone()
            if record is None:
                break
            print(f'{a}: {record.ProductName} - {record.UnitPrice}')
    def bottom_10_price(self):
        a = 0
        query = 'SELECT top 10 * FROM Products ORDER BY UnitPrice asc'
        data = self.sql_query(query)
        while True:
            a += 1
            record = data.fetchone()
            if record is None:
                break
            print(f'{a}: {record.ProductName} - {record.UnitPrice}')