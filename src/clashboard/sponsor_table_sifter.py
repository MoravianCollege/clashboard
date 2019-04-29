import pandas as pd
import os
import psycopg2
from pathlib import Path
from dotenv import load_dotenv


class SponsorTableSifter:
    TEST_DATA_DIR = Path(__file__).resolve().parent.parent.parent / 'tests/data'

    def __init__(self):
        load_dotenv()
        self.conn = None
        self.raw_sponsor_table = pd.DataFrame()
        self.sifted_sponsors_table = pd.DataFrame()
        self.hostname = os.getenv('hostname')
        self.port = os.getenv('port')
        self.database = os.getenv('database')
        self.username = os.getenv('username')
        self.password = os.getenv('password')

    def make_connection(self):
        print('Establishing connection to local database...\n')
        self.conn = psycopg2.connect(host=self.hostname,
                                     database=self.database,
                                     user=self.username,
                                     password=self.password)

    def query_database(self):
        print('Collecting Data from local Database...\n')
        sql_command = 'SELECT * from ctgov.sponsors'
        self.raw_sponsor_table = pd.read_sql(sql=sql_command, con=self.conn)

    def sift_leads(self):
        print('Removing duplicate sponsors...\n')
        self.sifted_sponsors_table = self.raw_sponsor_table.groupby('nct_id').filter(lambda x: len(x) > 2)\
            .drop_duplicates(subset='nct_id')

    def curate_all_sponsors(self):
        print('Checking names against known sponsors, and creating new column.\n')
        sponsor_names = {'Merck', 'Pfizer', 'NCI'}

        self.sifted_sponsors_table = self.raw_sponsor_table
        self.sifted_sponsors_table['curated_sponsors'] = pd.Series()

        for index in self.sifted_sponsors_table.index:
            for name in sponsor_names:
                if name in self.sifted_sponsors_table['name'][index]:
                    self.sifted_sponsors_table['curated_sponsors'][index] = name
                else:
                    self.sifted_sponsors_table['curated_sponsors'][index] = 'Other'

    def publish_table(self):
        print('Publishing new table to local database.\n')
        self.sifted_sponsors_table=self.sifted_sponsors_table[['nct_id', 'curated_sponsors']]
        self.sifted_sponsors_table.to_sql(name='curated_sponsors_table', con=self.conn)

    def create_curated_sponsors_column(self):
        self.make_connection()
        self.query_database()
        self.sift_leads()
        self.curate_all_sponsors()
        self.publish_table()
        print('Done.')
