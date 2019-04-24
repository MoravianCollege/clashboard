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
        sql_command = 'SELECT * from ctgov.sponsors'
        self.conn = psycopg2.connect(host=self.hostname,
                                     database=self.database,
                                     user=self.username,
                                     password=self.password)
        self.raw_sponsor_table = pd.read_sql(sql=sql_command, con=self.conn)

    def sift_leads(self):
        self.sifted_sponsors_table = self.raw_sponsor_table.groupby('nct_id').filter(lambda x: len(x) > 2)\
            .drop_duplicates(subset='nct_id')

    def sift_sponsors(self):
        self.sifted_sponsors_table = self.raw_sponsor_table
        self.sifted_sponsors_table['Sifted_Sponsors'] = self.sifted_sponsors_table['name'].str.contains('Merck')
        self.sifted_sponsors_table['Sifted_Sponsors'] = self.sifted_sponsors_table['Sifted_Sponsors']\
            .map({True: 'Merck', False: 'Other'})

    def curate_all_sponsors(self):
        sponsor_names = {'Merck', 'Phiser', 'Aventis', 'NCI'}

        self.sifted_sponsors_table = self.raw_sponsor_table

        for name in sponsor_names:
            self.sifted_sponsors_table['Sifted_Sponsors'] = self.sifted_sponsors_table['name']\
                .str.contains(name)

            self.sifted_sponsors_table['Sifted_Sponsors'] = self.sifted_sponsors_table['Sifted_Sponsors'] \
                .map({True: name})

    def publish_table(self):
        self.sifted_sponsors_table.to_sql(name='curated_sponsors', con=self.conn)

    def create_curated_sponsors_column(self):
        self.make_connection()
        self.sift_leads()
        self.curate_all_sponsors()
        self.publish_table()
