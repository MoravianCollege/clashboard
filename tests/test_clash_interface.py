
from clashboard.clash_interface import ClashInterface
from tests.mocks.mock_db import MockDB


def test_new_instance_has_no_group():

    db = MockDB()
    clash = ClashInterface(db)
    assert clash.get_group_by() == ''
