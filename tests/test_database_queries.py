from clashboard.clinical_database import ClinicalTrialsQuery
from pathlib import Path
import pandas as pd

TEST_DATA_DIR = Path(__file__).resolve().parent / 'data'


def mock_query(self):
    self.trials_data = pd.read_csv('{}/trial_test_data.csv'.format(TEST_DATA_DIR))
    self.sql_command = 'SELECT * FROM ctgov.studies'
    self.is_called = False


def set_up_tests(monkeypatch):
    monkeypatch.setattr(ClinicalTrialsQuery, 'db_query',
                        mock_query)
    ctd = ClinicalTrialsQuery()
    ctd.db_query()
    return ctd


def test_query_no_params():
    assert None == ClinicalTrialsQuery.db_query()


def test_no_data_update():
     assert None == ClinicalTrialsQuery.update_data('phase')



