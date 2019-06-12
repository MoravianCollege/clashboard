from clashboard.clinical_database import ClinicalDataCollector
from unittest.mock import patch
from pathlib import Path
import pandas as pd
import os
from datetime import datetime
import time

class_location = 'clashboard.clinical_database.ClinicalDataCollector.'
TEST_DATA_DIR = Path(__file__).resolve().parent / 'data'


def setup_env_vars(cdc):
    return (cdc.hostname == os.environ['hostname'] and
            cdc.port == os.environ['port'] and
            cdc.database == os.environ['database'] and
            cdc.username == os.environ['username'] and
            cdc.password == os.environ['password'])


def proper_setup():
    with patch.dict('os.environ', {'hostname': '127.0.0.1', 'port': '0000',
                                   'database': 'AACT', 'username': 'admin',
                                   'password': 'passterm'}):
        cdc = ClinicalDataCollector()
        assert setup_env_vars(cdc)
        return cdc


def mock_update_data():
    return pd.read_csv('{}/trial_test_data.csv'.format(TEST_DATA_DIR))


@patch('psycopg2.connect')
@patch('pandas.read_sql', side_effect=[mock_update_data()])
def test_complete_call(mock_conn, mock_sql):
    cdc = proper_setup()
    actual_data = mock_update_data()
    assert cdc.gather_data('study_type', []).equals(
        actual_data.groupby('study_type').size())


def test_initialize_data_empty():
    cdc = proper_setup()


def test_gather_data_empty():
    cdc = proper_setup()
    assert cdc.gather_data() is None


@patch(class_location+'query_data')
@patch(class_location+'update_data')
def test_gather_data_group(mock_query, mock_update):
    cdc = proper_setup()
    cdc.gather_data('study_type')
    assert mock_query.called
    assert mock_update.called


@patch(class_location + 'query_data')
@patch(class_location + 'update_data')
def test_gather_data_group_filter(mock_query, mock_update):
    filters = [['Phase', 'Phase 1']]
    cdc = proper_setup()
    cdc.gather_data('study_type', filters)
    assert mock_query.called
    assert mock_update.called


def test_gather_data_gather_twice_query_once():
    cdc = proper_setup()
    with patch(class_location + 'query_data') as mock_query:
        with patch(class_location + 'update_data') as mock_update:
            cdc.gather_data('study_type')
            assert mock_query.called
            assert mock_update.called
            mock_query.reset_mock()
            mock_update.reset_mock()
            cdc.gather_data('Phase')
            assert mock_query.called
            assert mock_update.called


def test_gather_data_gather_twice_query_twice():
    cdc = proper_setup()
    filters = [['Phase', 'Phase 1']]
    with patch(class_location + 'query_data') as mock_query:
        with patch(class_location + 'update_data') as mock_update:
            cdc.gather_data('study_type')
            assert mock_query.called
            assert mock_update.called
            mock_query.reset_mock()
            mock_update.reset_mock()
            cdc.gather_data('study_type', filters)
            assert mock_query.called
            assert mock_update.called


@patch(class_location+'create_query')
@patch(class_location+'make_connection')
def test_query_data_calling(mock_create, mock_conn):
    cdc = proper_setup()
    cdc.query_data()
    assert mock_create.called
    assert mock_conn.called


@patch(class_location+'make_local_table', side_effect=['studies'])
@patch(class_location+'add_filters', side_effect=[''])
def test_create_query_empty(mock_table, mock_filters):
    cdc = proper_setup()
    result_query = cdc.create_query()
    assert mock_table.called
    assert mock_filters.called
    assert result_query == 'SELECT * FROM studies'


def test_add_one_filter():
    cdc = proper_setup()
    filters = [['Phase', 'Phase 1']]
    assert cdc.add_filters(filters) == " WHERE Phase = 'Phase 1'"


def test_add_many_filter():
    cdc = proper_setup()
    filters = [['Phase', 'Phase 1'], ['study_type', 'Interventional']]
    assert cdc.add_filters(filters) == " WHERE Phase = 'Phase 1' AND " \
                                       "study_type = 'Interventional'"


def test_local_table():
    cdc = proper_setup()
    table = cdc.make_local_table('studies', True)
    assert table == 'ctgov.studies'


def test_remote_table():
    cdc = proper_setup()
    table = cdc.make_local_table('studies')
    assert table == 'studies'


@patch('psycopg2.connect')
def test_make_connection(mock):
    cdc = proper_setup()
    cdc.make_connection()
    assert mock.called
    mock.assert_called_with(database='AACT', host='127.0.0.1',
                            password='passterm', user='admin')


@patch('pandas.read_sql', side_effect=['data'])
def test_fetch_data(mock_sql):
    cdc = proper_setup()
    trials_data = cdc.fetch_sql_data('sql command')
    assert mock_sql.called
    mock_sql.assert_called_with(sql='sql command', con=None)
    assert trials_data == 'data'


@patch(class_location+'fetch_sql_data', side_effect=[pd.DataFrame()])
@patch('pandas.DataFrame.groupby', side_effect=['grouped'])
def test_update_grouping(mock_fetch_sql_data, mock_groupby):
    cdc = proper_setup()
    group = 'study_type'
    assert cdc.update_data(group) == 'grouped'
    assert mock_groupby.called
    mock_groupby.assert_called_with('study_type')


def mock_recent_date():
    data = pd.read_csv('{}/trial_test_data.csv'.format(TEST_DATA_DIR))
    time_data = pd.DataFrame(data, columns=['updated_at'])
    return time_data


time_data = mock_recent_date()


@patch('pandas.read_sql', side_effect=[time_data])
@patch(class_location + 'make_connection')
@patch(class_location + 'make_local_table', side_effect=['studies'])
def test_recent_date_calls(mock_sql, mock_conn, mock_local_table):
    mock_data = mock_update_data()
    mock_data_date = pd.DataFrame(mock_data, columns=['updated_at'])
    mock_timestamp = time.mktime(datetime.strptime(
        mock_data_date['updated_at'][0], "%Y-%m-%d %H:%M:%S.%f").timetuple())
    cdc = proper_setup()
    recent_date = cdc.get_most_recent_date()
    assert mock_sql.called
    assert mock_conn.called
    assert recent_date == datetime.fromtimestamp(mock_timestamp)
