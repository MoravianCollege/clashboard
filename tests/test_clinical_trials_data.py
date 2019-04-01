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


def set_up_tests(monkeypatch):
    monkeypatch.setattr(ClinicalTrialsData, 'populate_tables',
                        mock_populate_tables)
    ctd = ClinicalTrialsData()
    ctd.populate_tables()
    return ctd


def test_get_some_data(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.get_group_by() == 'phase'
    assert ctd.get_values() == [1, 2, 3]
    assert ctd.get_labels() == ['Phase 2', 'Phase 3', 'Phase 4']
    assert ctd.get_current_filters() == []


def test_change_group_by_changes_data(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    ctd.set_group_by('study type')
    assert ctd.get_group_by() == 'study type'
    assert ctd.get_values() == [9, 1]
    labels = ['Interventional', 'Observational [Patient Registry]']
    assert ctd.get_labels() == labels
    assert ctd.get_current_filters() == []


def test_change_current_filters(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.get_current_filters() == []
    ctd.apply_filter('phase', 'Phase 1')
    assert ctd.get_current_filters() == [['phase', 'Phase 1']]
    ctd.remove_filter('phase', 'Phase 1')
    assert ctd.get_current_filters() == []
    ctd.apply_filter('study_type', 'Interventional')
    ctd.apply_filter('study_type', 'Observational [Patient Registry]')
    ctd.apply_filter('phase', 'Phase 2')
    filters = [['study type', 'Interventional'],
               ['study type', 'Observational [Patient Registry]'],
               ['phase', 'Phase 2']]
    assert ctd.get_current_filters() == filters
    ctd.remove_filter('study type', 'Observational [Patient Registry]')
    assert ctd.get_current_filters() == [['study type', 'Interventional'],
                                         ['phase', 'Phase 2']]


def test_remove_from_empty_filters_list(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.get_current_filters() == []
    ctd.remove_filter('phase', 'Phase 1')


def test_remove_from_populated_filter(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    ctd.apply_filter('study_type', 'Interventional')
    ctd.apply_filter('study_type', 'Observational [Patient Registry]')
    ctd.apply_filter('phase', 'Phase 2')
    filters = [['study type', 'Interventional'],
               ['study type', 'Observational [Patient Registry]'],
               ['phase', 'Phase 2']]
    ctd.remove_filter('phase', 'Phase 1')
    assert ctd.get_current_filters() == filters


def test_remove_with_space_check(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    ctd.apply_filter('study type', 'Interventional')
    ctd.remove_filter('study type', 'Interventional')
    assert ctd.get_current_filters() == []


def test_apply_with_space_check(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    ctd.apply_filter('study type', 'Interventional')
    assert ctd.get_current_filters() == [['study type', 'Interventional']]


def test_replace_underscore(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.replace_underscore("study_type") == 'study type'


def test_replace_multiple_underscores(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.replace_underscore("last_known_status") == \
        "last known status"


def test_replace_space(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.replace_space('study type') == 'study_type'


def test_replace_multiple_spaces(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.replace_space('last known status') == \
        'last_known_status'


def set_get_group_by_with_space(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    ctd.set_group_by('study type')
    assert ctd.get_group_by() == 'study type'
