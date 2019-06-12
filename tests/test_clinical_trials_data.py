from clashboard.clinical_trials_data import ClinicalTrialsData
from clashboard.clinical_database import ClinicalDataCollector
from pathlib import Path
from datetime import date
import pandas as pd

TEST_DATA_DIR = Path(__file__).resolve().parent / 'data'


'''def mock_update_data(self, group):
    data = pd.read_csv('{}/trial_test_data.csv'.format(TEST_DATA_DIR))
    groupings = ['study_type', 'overall_status', 'phase',
                 'enrollment_type', 'last_known_status']
    if group in groupings:
        grouped_data = data.groupby(group).size()
        return list(grouped_data.index.values), list(grouped_data.values)
    return [], []'''


def mock_get_download_date(self):
    download_date = date(2019, 4, 13)
    return "{}/{}/{}".format(download_date.month,
                             download_date.day,
                             download_date.year)


def mock_gather_data(self, group='', filters=None):
    data = pd.read_csv('{}/trial_test_data.csv'.format(TEST_DATA_DIR))
    return data.groupby(group).size()


def set_up_tests(monkeypatch):
    '''monkeypatch.setattr(ClinicalTrialsData, 'update_data',
                        mock_update_data)'''
    monkeypatch.setattr(ClinicalTrialsData, 'get_download_date',
                        mock_get_download_date)
    monkeypatch.setattr(ClinicalDataCollector, 'gather_data',
                        mock_gather_data)
    ctd = ClinicalTrialsData()
    return ctd


def test_replace_underscore(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.replace_underscore("study_type") == 'Study Type'


def test_replace_multiple_underscores(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.replace_underscore("last_known_status") == \
        "Last Known Status"


def test_replace_space(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.replace_space('study type') == 'study_type'
    assert ctd.replace_space('Study Type') == 'study_type'


def test_replace_multiple_spaces(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.replace_space('last known status') == \
        'last_known_status'


def test_change_group_by_changes_dropdown(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    groupings = ['Study Type', 'Overall Status',
                 'Enrollment Type', 'Last Known Status']
    assert ctd.get_group_choices('phase') == groupings

    ctd = set_up_tests(monkeypatch)
    groupings = ['Overall Status', 'Phase',
                 'Enrollment Type', 'Last Known Status']
    ctd.compute_results('Study Type', [])
    assert ctd.get_group_choices('study_type') == groupings


def test_get_download_date(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.get_download_date() == "4/13/2019"


def test_update_data_empty_lists(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.update_data('') == ([], [])


def test_update_data(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.update_data('study_type', []) == (['Interventional',
               'Observational [Patient Registry]'], [9, 1])


def test_compute_results_bad_first_parameter(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    group = ''
    assert ctd.compute_results(group, []) == ([], [])


'''def test_compute_results_group_filter_within_values(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    filters = ['Interventional',
               'Observational [Patient Registry]',
               'Phase 2']
    group = 'Overall Status'
    group_filter = [['study_type', 'Interventional'],
                    ['study_type', 'Observational [Patient Registry]'],
                    ['phase', 'Phase 2']]
    ctd.compute_results(group, group_filter)
    for item in ctd.filters:
        filter_name = item[1]
        assert filter_name in filters'''
