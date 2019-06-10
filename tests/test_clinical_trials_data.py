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


def test_new_instance_produces_empty_data():
    ctd = ClinicalTrialsData()
    assert ctd.get_group_by() == ''
    assert ctd.get_current_filters() == []
    assert ctd.get_labels() == []
    assert ctd.get_values() == []


def set_up_tests(monkeypatch):
    monkeypatch.setattr(ClinicalTrialsData, 'update_data',
                        mock_update_data)
    monkeypatch.setattr(ClinicalTrialsData, 'get_download_date',
                        mock_get_download_date)
    ctd = ClinicalTrialsData()
    ctd.update_data('phase')
    return ctd


def test_get_some_data(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.get_group_by() == 'Phase'
    assert ctd.get_values() == [1, 2, 3]
    assert ctd.get_labels() == ['Phase 2', 'Phase 3', 'Phase 4']
    assert ctd.get_current_filters() == []


def test_change_group_by_changes_data(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    ctd.set_group_by('study type')
    ctd.update_data('study_type')
    assert ctd.get_group_by() == 'Study Type'
    assert ctd.get_values() == [9, 1]
    labels = ['Interventional', 'Observational [Patient Registry]']
    assert ctd.get_labels() == labels
    assert ctd.get_current_filters() == []


def test_change_current_filters(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.get_current_filters() == []
    ctd.apply_filter('phase', 'Phase 1')
    assert ctd.get_current_filters() == [['Phase', 'Phase 1']]
    ctd.remove_filter('phase', 'Phase 1')
    assert ctd.get_current_filters() == []
    ctd.apply_filter('study_type', 'Interventional')
    ctd.apply_filter('study_type', 'Observational [Patient Registry]')
    ctd.apply_filter('phase', 'Phase 2')
    filters = [['Study Type', 'Interventional'],
               ['Study Type', 'Observational [Patient Registry]'],
               ['Phase', 'Phase 2']]
    assert ctd.get_current_filters() == filters
    ctd.remove_filter('study type', 'Observational [Patient Registry]')
    assert ctd.get_current_filters() == [['Study Type', 'Interventional'],
                                         ['Phase', 'Phase 2']]


def test_remove_from_empty_filters_list(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    assert ctd.get_current_filters() == []
    ctd.remove_filter('phase', 'Phase 1')


def test_remove_from_populated_filter(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    ctd.apply_filter('study_type', 'Interventional')
    ctd.apply_filter('study_type', 'Observational [Patient Registry]')
    ctd.apply_filter('phase', 'Phase 2')
    filters = [['Study Type', 'Interventional'],
               ['Study Type', 'Observational [Patient Registry]'],
               ['Phase', 'Phase 2']]
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
    assert ctd.get_current_filters() == [['Study Type', 'Interventional']]


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


def set_get_group_by_with_space(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    ctd.set_group_by('study type')
    assert ctd.get_group_by() == 'study type'


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


def test_compute_results_grouping(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    group = 'overall_status'
    assert ctd.compute_results(group, []) == \
        (ctd.get_labels(), ctd.get_values())
    assert ctd.get_values() == [8, 1, 1]
    assert ctd.get_labels() == ['Completed', 'Recruiting', 'Suspended']


def test_compute_results_filters(monkeypatch):
    ctd = set_up_tests(monkeypatch)
    group = 'overall_status'
    group_filter = [['study_type', 'Interventional']]
    ctd.compute_results(group, group_filter)
    assert ctd.filters == group_filter
