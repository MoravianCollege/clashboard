from clashboard.sponsor_table_sifter import SponsorTableSifter
import pandas as pd


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
    assert not pd.DataFrame.equals(ts.sifted_sponsors_table, ts.raw_sponsor_table)


def test_get_merck_only():
    ts = load_csv()
    ts.sift_leads()
    comparison_table = ts.sifted_sponsors_table
    ts.sift_sponsors()
    assert not pd.DataFrame.equals(comparison_table, ts.sifted_sponsors_table)
