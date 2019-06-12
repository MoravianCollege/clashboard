import pandas as pd
import datetime
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
        data = pd.read_csv(self.file).groupby(group).size()

        if group == data.index.name:
            values = list(data.values)

        if group == data.index.name:
            labels = list(data.index)

        return labels, values
