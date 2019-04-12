import pandas as pd
from clashboard.clinical_trials_data import ClinicalTrialsData


class MockClinicalTrialsData(ClinicalTrialsData):
    """
    This class allows for easy GUI testing.  Rather than load data
    from the database, we load it from a CSV file.
    """
    def __init__(self, filename):
        super().__init__()
        self.file = filename

    def update_data(self, group):
        self.studies = pd.read_csv(self.file).groupby(group).size()
