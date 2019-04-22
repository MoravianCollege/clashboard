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
        self.sifted_sponsors_table = self.raw_sponsor_table[self.raw_sponsor_table['lead_or_collaborator'].str.contains('lead')].groupby('nct_id')
        return self.sifted_sponsors_table

    def sift_sponsors(self):
        self.sifted_sponsors_table = self.sifted_sponsors_table[self.sifted_sponsors_table['name'].str.contains('Merck')]
        return self.sifted_sponsors_table

