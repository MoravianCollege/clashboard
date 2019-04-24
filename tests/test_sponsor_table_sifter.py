from clashboard.sponsor_table_sifter import SponsorTableSifter
import pandas as pd
import csv


def load_csv():
    ts = SponsorTableSifter()
    ts.make_connection()
    return ts


def test_establish_base_table():
    ts = load_csv()
    assert not ts.raw_sponsor_table.empty


def test_get_leads_only():
    ts = load_csv()
    ts.sift_leads()
    dif = pd.DataFrame.equals(ts.sifted_sponsors_table, ts.raw_sponsor_table)
    assert not dif


def test_get_merck_only():
    ts = load_csv()
    ts.sift_leads()
    comparison_table = ts.sifted_sponsors_table
    ts.sift_sponsors()
    assert not pd.DataFrame.equals(comparison_table, ts.sifted_sponsors_table)


def test_write_to_csv():
    ts = load_csv()
    file_path = '{}/100_curated_sponsors.csv'.format(ts.TEST_DATA_DIR)
    ts.sift_leads()
    ts.sift_sponsors()
    ts.publish_table()
    assert is_csv_filled(file_path)


def is_csv_filled(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count > 1:
                break
        return line_count > 1


def test_complete_process():
    ts = load_csv()
    file_path = '{}/100_curated_sponsors.csv'.format(ts.TEST_DATA_DIR)
    ts.create_curated_sponsors_column()
    assert is_csv_filled(file_path)
