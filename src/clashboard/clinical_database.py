import pandas as pd
import os
import psycopg2


class ClinicalTrialsQuery:

    def __init__(self):
        self.sql_command = ''
        self.trials_data = pd.DataFrame()
        self.is_called = False
        self.hostname = os.getenv('hostname')
        self.port = os.getenv('port')
        self.database = os.getenv('database')
        self.username = os.getenv('username')
        self.password = os.getenv('password')

    def db_query(self, filters=[], group=''):
        """
        New SQL query
        :param filters:
        :param group:
        :return:
        """
        self.sql_command = 'SELECT * FROM ' + self.make_local_table()
        self.is_called = True
        self.trials_data = pd.read_sql(sql=self.sql_command, con=psycopg2.connect(host=self.hostname,
                                                                                  database=self.database,
                                                                                  user=self.username,
                                                                                  password=self.password))
        return self.trials_data

    def make_local_table(self, table = '', local=True):
        return 'ctgov.' + table

    def update_data(self, group='phase'):
        """
        Update Group By
        :param group:
        :return:
        """
        return self.trials_data.groupby([group]) if self.is_called else None
