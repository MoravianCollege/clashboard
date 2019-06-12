from clashboard.clinical_trials_data import ClinicalTrialsData
from pathlib import Path
from datetime import date
import pandas as pd

TEST_DATA_DIR = Path(__file__).resolve().parent / 'data'


def mock_update_data(self, grouping):
    data = pd.read_csv('{}/trial_test_data.csv'.format(TEST_DATA_DIR))
    self.studies = data.groupby(grouping).size()
    self.curr_group = grouping


def mock_get_download_date(self):
    download_date = date(2019, 4, 13)
    return "{}/{}/{}".format(download_date.month,
                             download_date.day,
                             download_date.year)


def set_up_tests(monkeypatch):
    monkeypatch.setattr(ClinicalTrialsData, 'update_data',
                        mock_update_data)
    monkeypatch.setattr(ClinicalTrialsData, 'get_download_date',
                        mock_get_download_date)
    ctd = ClinicalTrialsData()
    ctd.update_data('phase')
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


def test_get_dropdown_choices(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    groupings = ['Study Type', 'Overall Status',
                 'Enrollment Type', 'Last Known Status']
    assert ctd.get_group_choices() == groupings


def test_get_dropdown_choices_with_group_by(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    groupings = ['Overall Status', 'Phase',
                 'Enrollment Type', 'Last Known Status']
    ctd.set_group_by('Study Type')
    assert ctd.get_group_choices() == groupings


def test_change_group_by_changes_dropdown(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    groupings = ['Study Type', 'Phase', 'Enrollment Type', 'Last Known Status']
    ctd.set_group_by('Overall Status')
    assert ctd.get_group_choices() == groupings
    new_groupings = ['Study Type', 'Overall Status',
                     'Enrollment Type', 'Last Known Status']
    ctd.set_group_by('Phase')
    assert ctd.get_group_choices() == new_groupings


def test_get_download_date(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.get_download_date() == "4/13/2019"


def test_compute_results_change_group(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    group = 'overall_status'
    ctd.compute_results(group, [])
    assert ctd.curr_group == group


def test_compute_results_filters(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    group = 'Overall Status'
    group_filter = [('Study Type', 'Interventional')]
    computed_filter = [('study_type', 'Interventional')]
    ctd.compute_results(group, group_filter)
    assert ctd.filters == computed_filter


def test_compute_results_bad_first_parameter(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    group = ''
    assert ctd.compute_results(group, []) == ([], [])


def test_compute_results_filter_is_list(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    group = 'Overall Status'
    group_filter = [('Study Type', 'Interventional')]
    ctd.compute_results(group, group_filter)
    assert type(ctd.filters) == list


def test_compute_results_group_filter_within_values(monkeypatch):
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
        assert filter_name in filters
