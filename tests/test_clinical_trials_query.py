from clashboard.clinical_database import *
from unittest.mock import patch


@patch('clashboard.clinical_database.fetch_sql_data')
@patch('clashboard.clinical_database.make_connection')
def test_gather_data_missing_group(mock1, mock2):
    data = gather_data('')
    assert data is None
    assert mock1.called is False
    assert mock2.called is False


@patch('clashboard.clinical_database.query_data')
@patch('clashboard.clinical_database.update_data')
@patch('pandas.DataFrame.size')
def test_gather_data_happy_path_query(query, update, size):
    data = gather_data('phase', [['phase', 'Phase 1']])
    assert query.called
    assert update.called
    assert size.called


@patch('clashboard.clinical_database.query_data')
@patch('clashboard.clinical_database.update_data')
@patch('pandas.DataFrame.size')
def test_gather_data_happy_path_no_query(query, update, size):
    first = gather_data('phase')
    assert update.called
    assert size.called
    with patch('clashboard.clinical_database.query_data') as no_query:
        data = gather_data('study_type')
        assert no_query.called is False


@patch('clashboard.clinical_database.create_query')
@patch('clashboard.clinical_database.make_connection')
@patch('clashboard.clinical_database.fetch_sql_data')
def test_query_data(create, conn, fetch):
    query_data()
    assert create.called
    assert conn.called
    assert fetch.called


def test_create_query():
    sql_command = create_query()
    assert sql_command == 'SELECT * FROM studies'


def test_remote_table():
    table = make_local_table('studies')
    assert table == 'studies'


def test_local_table():
    table = make_local_table('studies', True)
    assert table == 'ctgov.studies'


@patch('psycopg2.connect')
def test_make_connection(mock):
    make_connection()
    assert mock.called


@patch('pandas.read_sql')
def test_fetch_data(mock):
    data = fetch_sql_data('')
    assert mock.called


@patch('pandas.DataFrame.groupby')
def test_update_data(mock):
    data = update_data()
    assert mock.called





