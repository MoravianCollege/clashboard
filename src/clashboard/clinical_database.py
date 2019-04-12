import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv


trials_data = pd.DataFrame()
load_dotenv()
hostname = os.getenv('hostname')
port = os.getenv('port')
database = os.getenv('database')
username = os.getenv('username')
password = os.getenv('password')
conn = None
filters = []
group = None


def gather_data(new_group, new_filters=[]):
    global conn, filters, group, trials_data
    if new_group == '':
        return None
    need_query = (group is None) or \
                 (filters != new_filters)
    filters = new_filters
    group = new_group
    if need_query:
        query_data()
    return update_data().size()


def query_data():
    sql_command = create_query()
    make_connection()
    fetch_sql_data(sql_command)


def create_query():
    sql_command = 'SELECT * FROM ' + make_local_table('studies', False)
    # add_filters()
    return sql_command


# def add_filters(sql_command):
#     global filters
#     sql_command += " WHERE " if len(filters) > 0 else ''
#     for name in filters:
#         sql_command += name[0] + "='" + name[1] + "'"
#     return sql_command


def make_local_table(table, local=False):
    return 'ctgov.' + table if local else table


def make_connection():
    global hostname, database, username, password, conn
    conn = psycopg2.connect(host=hostname,
                            database=database,
                            user=username,
                            password=password)


def fetch_sql_data(sql_command):
    global conn, trials_data
    trials_data = pd.read_sql(sql=sql_command, con=conn)


def update_data():
    global group, trials_data
    return trials_data.groupby(group)
