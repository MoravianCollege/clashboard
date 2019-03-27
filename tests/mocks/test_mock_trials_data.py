from pathlib import Path
from tests.mocks.mock_trials_data import MockClinicalTrialsData

TEST_DATA_DIR = Path(__file__).resolve().parent.parent / 'data'


def test_data_read_from_standard_file():
    file_path = '{}/trial_test_data.csv'.format(TEST_DATA_DIR)
    mctd = MockClinicalTrialsData(file_path)
    mctd.populate_tables()
    mctd.set_group_by('study_type')
    assert mctd.get_group_by() == 'study_type'
    assert mctd.get_values() == [9, 1]
    labels = ['Interventional', 'Observational [Patient Registry]']
    assert mctd.get_labels() == labels
    assert mctd.get_current_filters() == []
