from dotenv import load_dotenv
import pandas as pd
import psycopg2
import os


class ClinicalDataCollector:

    def __init__(self):
        load_dotenv()
        self.hostname = os.getenv('hostname')
        self.port = os.getenv('port')
        self.database = os.getenv('database')
        self.username = os.getenv('username')
        self.password = os.getenv('password')
        self.conn = None
        self.filters = []
        self.group = None
        self.trials_data = pd.DataFrame()

    def gather_data(self, new_group='', new_filters=None):
        if new_filters is None:
            new_filters = []
        if new_group == '':
            return None
        need_query = (self.group is None) or \
                     (self.filters != new_filters)
        self.filters = new_filters[:]
        self.group = new_group
        if need_query:
            self.query_data()
        return self.update_data().size()

    def query_data(self):
        sql_command = self.create_query()
        self.make_connection()
        self.fetch_sql_data(sql_command)

    def create_query(self):
        sql_command = 'SELECT * FROM ' + \
                      self.make_local_table('studies', False)
        sql_command += self.add_filters()
        return sql_command

    def add_filters(self):
        sql_filters = " WHERE " if len(self.filters) > 0 else ''
        for i, name in enumerate(self.filters, 1):
            sql_filters += name[0] + " = '" + name[1] + "'"
            if i < len(self.filters):
                sql_filters += " AND "
        return sql_filters

    def make_local_table(self, table, local=False):
        return 'ctgov.' + table if local else table

    def make_connection(self):
        self.conn = psycopg2.connect(host=self.hostname,
                                     database=self.database,
                                     user=self.username,
                                     password=self.password)

    def fetch_sql_data(self, sql_command):
        self.trials_data = pd.read_sql(sql=sql_command, con=self.conn)

    def update_data(self):
        return self.trials_data.groupby(self.group)
