
from tests.mocks.mock_trials_data import MockClinicalTrialsData


def test_new_instance_has_no_group():

    mctd = MockClinicalTrialsData()
    assert mctd.get_group_by() == ''


def test_change_group_by():

    mctd = MockClinicalTrialsData()
    mctd.populate_tables()
    assert mctd.get_group_by() == ''
    mctd.set_group_by('study_type')
    assert mctd.get_group_by() == 'study_type'


def test_get_some_data():

    mctd = MockClinicalTrialsData()
    mctd.populate_tables()
    mctd.set_group_by('phase')
    assert mctd.get_labels()[0] == 'Phase 2'
    assert mctd.get_labels()[1] == 'Phase 3'
    assert mctd.get_labels()[2] == 'Phase 4'
    assert mctd.get_values()[0] == 1
    assert mctd.get_values()[1] == 2
    assert mctd.get_values()[2] == 3
