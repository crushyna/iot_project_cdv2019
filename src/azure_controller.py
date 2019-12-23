import pyodbc


class AzureController:

    def __init__(self):
        self.server = 'sqlserveracs.database.windows.net'
        self.database = 'AccessControl'
        self.username = 'adminkamil'
        self.password = 'CDVprojekt2019!'
        self.driver = '{ODBC Driver 17 for SQL Server}'

    # execute specific query
    def execute_query(self, query_string: str):
        cnxn = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = cnxn.cursor()
        cursor.execute(query_string)
        row = cursor.fetchone()
        while row:
            for each_row in row:
                print(each_row)

            row = cursor.fetchone()

    @staticmethod
    def change_user_status(user_id, card_string):
        print(user_id)
        print(card_string)
        pass
