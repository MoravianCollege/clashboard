from clashboard.sponsor_table_sifter import SponsorTableSifter


def load_csv():
    ts = SponsorTableSifter()
    ts.make_connection()
    return ts


def test_get_leads_only():
    ts = load_csv()
    ts.sift_leads()
