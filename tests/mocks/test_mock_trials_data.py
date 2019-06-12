from pathlib import Path
from tests.mocks.mock_trials_data import MockClinicalTrialsData

TEST_DATA_DIR = Path(__file__).resolve().parent.parent / 'data'


def test_data_read_from_standard_file():
    file_path = '{}/trial_test_data.csv'.format(TEST_DATA_DIR)
    mctd = MockClinicalTrialsData(file_path)
    data = mctd.compute_results('Study Type', [])
    assert mctd.get_current_filters() == []
    labels = ['Interventional', 'Observational [Patient Registry]']
    assert mctd.update_data('study_type') == (labels, [9, 1])
    assert data == (labels, [9, 1])
