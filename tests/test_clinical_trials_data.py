
from clashboard.clinical_trials_data import ClinicalTrialsData
from tests.mocks.mock_db import MockDB


def test_new_instance_has_no_group():

    db = MockDB(None)
    clash = ClinicalTrialsData(db, None)
    assert clash.get_group_by() == 'phase'


def test_change_group_by():

    db = MockDB(None)
    clash = ClinicalTrialsData(db, None)
    assert clash.get_group_by() == 'phase'
    clash.set_group_by('study_type')
    assert clash.get_group_by() == 'study_type'

# def test_get_some_data():
#
#    db = MockDB('mocks/trial_test_data.csv')
#    db.populate_tables()
#    clash = ClinicalTrialsData(db, None)
