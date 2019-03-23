
from clashboard.clinical_trials_data import ClinicalTrialsData
from pathlib import Path
import pandas as pd

TEST_DATA_DIR = Path(__file__).resolve().parent / 'data'


def mock_populate_tables(self):
    self.studies = pd.read_csv('{}/trial_test_data.csv'.format(TEST_DATA_DIR))
    self.curr_group = 'phase'


def test_new_instance_produces_empty_data():
    ctd = ClinicalTrialsData()
    assert ctd.get_group_by() == ''
    assert ctd.get_current_filters() == []
    assert ctd.get_labels() == []
    assert ctd.get_values() == []


def test_get_some_data(monkeypatch):
    monkeypatch.setattr(ClinicalTrialsData, 'populate_tables', mock_populate_tables)
    ctd = ClinicalTrialsData()
    ctd.populate_tables()
    assert ctd.get_group_by() == 'phase'
    assert ctd.get_values() == [1, 2, 3]
    assert ctd.get_labels() == ['Phase 2', 'Phase 3', 'Phase 4']
    assert ctd.get_current_filters() == []


def test_change_group_by_changes_data(monkeypatch):
    monkeypatch.setattr(ClinicalTrialsData, 'populate_tables', mock_populate_tables)
    ctd = ClinicalTrialsData()
    ctd.populate_tables()
    ctd.set_group_by('study_type')
    assert ctd.get_group_by() == 'study_type'
    assert ctd.get_values() == [9, 1]
    assert ctd.get_labels() == ['Interventional', 'Observational [Patient Registry]']
    assert ctd.get_current_filters() == []


