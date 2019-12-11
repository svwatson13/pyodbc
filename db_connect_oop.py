import pyodbc

class MSDBConnection():
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'

        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                               +self.server+';DATABASE='+self.database+';UID='+
                                               self.username+';PWD='+ self.password)
        self.cursor = self.docker_Northwind.cursor()

    def sql_query(self, sql_query):
        return self.cursor.execute(sql_query) # Makes it private - can only be called by other methods

