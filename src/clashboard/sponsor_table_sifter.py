import pandas as pd
from pathlib import Path


class SponsorTableSifter:
    TEST_DATA_DIR = Path(__file__).resolve().parent.parent.parent / 'tests/data'

    def __init__(self):
        self.conn = None
        self.raw_sponsor_table = pd.DataFrame()
        self.sifted_sponsors_table = pd.DataFrame()

    def make_connection(self):
        file_path = '{}/100_sponsors_table.csv'.format(self.TEST_DATA_DIR)
        self.raw_sponsor_table = pd.read_csv(file_path)

    def sift_leads(self):
        self.sifted_sponsors_table = self.raw_sponsor_table.groupby('nct_id').filter(lambda x: len(x) > 2)\
            .drop_duplicates(subset='nct_id')

    def sift_sponsors(self):
        self.sifted_sponsors_table = self.raw_sponsor_table
        self.sifted_sponsors_table['Sifted_Sponsors'] = self.sifted_sponsors_table['name'].str.contains('Merck')
        self.sifted_sponsors_table['Sifted_Sponsors'] = self.sifted_sponsors_table['Sifted_Sponsors']\
            .map({True: 'Merck', False: 'Other'})

    def publish_table(self):
        file_path = '{}/100_curated_sponsors.csv'.format(self.TEST_DATA_DIR)
        self.sifted_sponsors_table.to_csv(path_or_buf=file_path)

    def create_curated_sponsors_column(self):
        self.make_connection()
        self.sift_leads()
        self.sift_sponsors()
        self.publish_table()
