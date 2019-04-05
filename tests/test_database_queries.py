from clashboard.clinical_database import ClinicalTrialsQuery
from pathlib import Path
import pandas as pd

TEST_DATA_DIR = Path(__file__).resolve().parent / 'data'


def mock_query(self):
    file_location = '{}/trial_test_data.csv'
    self.trials_data = pd.read_csv(file_location.format(TEST_DATA_DIR))
    self.sql_command = 'SELECT * FROM ctgov.studies'
    self.is_called = True


def set_up_tests(monkeypatch):
    monkeypatch.setattr(ClinicalTrialsQuery, 'db_query', mock_query)
    ctd = ClinicalTrialsQuery()
    ctd.db_query()
    return ctd


def test_query_no_params(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.db_query() is None


def test_no_data_update():
    assert ClinicalTrialsQuery().update_data('phase') is None


def test_correct_data(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    results = pd.read_csv('{}/trial_test_data.csv'.format(TEST_DATA_DIR))
    assert len(results) == len(ctd.trials_data)


def test_local_table():
    ctd = ClinicalTrialsQuery()
    assert 'ctgov.studies' == ctd.make_local_table('studies', True)


def test_remote_table():
    ctd = ClinicalTrialsQuery()
    assert 'studies' == ctd.make_local_table('studies', False)


def test_query_groupby(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    results = pd.read_csv('{}/trial_test_data.csv'.format(TEST_DATA_DIR))
    data = ctd.db_query()
    grouped_data = ctd.update_data()
    assert len(results.groupby(['phase'])) == len(grouped_data)
