from dotenv import load_dotenv
import pandas as pd
import psycopg2
import os
from datetime import datetime
import time


class ClinicalDataCollector:

    def __init__(self):
        load_dotenv()
        self.hostname = os.getenv('hostname')
        self.port = os.getenv('port')
        self.database = os.getenv('database')
        self.username = os.getenv('username')
        self.password = os.getenv('password')
        self.conn = None
        self.trials_data = pd.DataFrame()


    def gather_data(self, group='', filters=None):
        if group == '':
            return None
        self.query_data(filters)
        return self.update_data(group).size()

    def query_data(self, filters=[]):
        sql_command = self.create_query(filters)
        self.make_connection()
        self.fetch_sql_data(sql_command)

    def create_query(self, filters=[]):
        sql_command = 'SELECT * FROM ' + \
                      self.make_local_table('studies', False)
        sql_command += self.add_filters(filters)
        return sql_command

    def add_filters(self, filters=[]):
        sql_filters = " WHERE " if len(filters) > 0 else ''
        for i, name in enumerate(filters, 1):
            sql_filters += name[0] + " = '" + name[1] + "'"
            if i < len(filters):
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

    def update_data(self, group=''):
        return self.trials_data.groupby(group)

    def get_most_recent_date(self):
        if self.conn is None:
            self.make_connection()
        sql_command = "SELECT updated_at from " + \
                      self.make_local_table('studies', False)
        recent_data = pd.read_sql(sql_command, con=self.conn)
        timestamp = recent_data['updated_at'][0]
        datetime_object = time.mktime(
            datetime.strptime(str(timestamp),
                              "%Y-%m-%d %H:%M:%S.%f").timetuple())
        return datetime.fromtimestamp(datetime_object)
