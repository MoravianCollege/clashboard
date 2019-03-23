import pandas as pd


class MockClinicalTrialsData:

    def __init__(self, filename='trial_test_data.csv'):
        self.file = filename
        self.studies = None
        self.curr_group = ''
        self.type_counts = None

    def populate_tables(self):
        self.studies = pd.read_csv(self.file)

    def set_group_by(self, attribute):
        self.curr_group = attribute
        self.type_counts = self.studies.groupby(self.curr_group).size()

    def get_group_by(self):
        return self.curr_group

    def get_labels(self):
        return self.type_counts.index

    def get_values(self):
        return self.type_counts.values
