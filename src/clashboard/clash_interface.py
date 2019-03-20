from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd


class ClashInterface:


    def __init__(self):
        self.conn = None
        self.data_table = None
        self.value_counts = None
        self.group_by = None
        self.filters = []

        load_dotenv()
        hostname = os.getenv('hostname')
        database = os.getenv('database')
        username = os.getenv('username')
        password = os.getenv('password')

        conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
        self.data_table = pd.read_sql('select * from studies', con=conn)

    def remove_filter(self, filter):
        pass

    def apply_filter(self, filter):
        pass

    def get_current_filters(self):
        return self.filters

    def set_group_by(self, attribute):
        pass

    def get_group_by(self):
        return self.group_by

    def get_labels(self):
        return self.value_counts.index

    def get_values(self):
        return self.value_counts.values

    def get_variables(self):
        return []
