import pyodbc


class AzureDBController:

    def __init__(self):
        self.server = 'sqlserveracs.database.windows.net'
        self.database = 'AccessControl'
        self.username = 'adminkamil'
        self.password = 'CDVprojekt2019!'
        self.driver = '{FreeTDS}'
        # self.driver = '{ODBC Driver 17 for SQL Server}'
        self.driver_version = '7.4'
        self.cnxn = pyodbc.connect(
            'DRIVER={0};SERVER={1};PORT=1433;DATABASE={2};UID={3};PWD={4};TDS_Version={5};'.format(self.driver, self.server,
                                                                                  self.database, self.username,
                                                                                  self.password, self.driver_version))
        '''
        self.cnxn = pyodbc.connect(
            'DRIVER={0};SERVER={1};PORT=1433;DATABASE={2};UID={3};PWD={4};'.format(self.driver, self.server,
                                                                                   self.database, self.username,
                                                                                   self.password))
                                                                                   '''

        self.cursor = self.cnxn.cursor()

    def execute_update(self, query_string: str):
        self.cursor.execute(query_string)
        self.cnxn.commit()

        print("Affected rows = {}".format(self.cursor.rowcount))

    def execute_select(self, query_string: str):
        self.cursor.execute(query_string)
        row = self.cursor.fetchall()
        for each_row in row:
            result = each_row[0]

        self.cursor.fetchone()
        return result

    def execute_query_multiple_rows(self, query_string: str):
        query_list = []
        self.cursor.execute(query_string)
        row = self.cursor.fetchone()
        while row:
            for each_row in row:
                query_list.append(each_row)
                print(each_row)

            row = self.cursor.fetchone()

        return query_list

    @staticmethod
    def switch_user_status(card_id: int, card_text: str):
        current_status = f"""SELECT [IsPresent]
                            FROM [dbo].[Persons]
                            WHERE [RfidCardId] = {card_id}
                            AND [RfidCardText] = '{card_text}';"""

        status = azuredb1.execute_select(current_status)

        if status:
            query1 = f"""UPDATE [dbo].[Persons]
                        SET [IsPresent] = 'False'
                        WHERE [RfidCardId] = {card_id}
                        AND [RfidCardText] = '{card_text}';"""

            azuredb1.execute_update(query1)
            print(f"{card_id}, {card_text}: IsPresent = False")

        else:
            query2 = f"""UPDATE [dbo].[Persons]
                        SET [IsPresent] = 'True'
                        WHERE [RfidCardId] = {card_id}
                        AND [RfidCardText] = '{card_text}';"""

            azuredb1.execute_update(query2)
            print(f"{card_id}, {card_text}: IsPresent = True")

    @staticmethod
    def check_user_access(card_id: int, card_text: str):
        query = f"""SELECT [HasAccess] 
                    FROM [dbo].[Persons]
                    WHERE [RfidCardId] = {card_id}
                    AND [RfidCardText] = '{card_text}'"""

        result = azuredb1.execute_select(query)

        return result

    # 329308361597
    # test1
    # azuredb1.check_user_access(329308361597, 'test1')
    # azuredb1.switch_user_status(329308361597, 'test1')


azuredb1 = AzureDBController()
azuredb1.switch_user_status(329308361597, 'test1')
