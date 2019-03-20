
from clashboard.clash_interface import ClashInterface


def test_new_instance_has_no_group():

    clash = ClashInterface()
    assert clash.get_group_by() == []
