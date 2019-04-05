from clashboard.clashboard_gui import add_filter,delete_filter

columns = [{'name': 'Filters', 'id': 'column-0', 'deletable': False, 'editable_name': False}]


def test_add_filter_empty_list():
    rows = []
    filter = 'Observational [Patient Registry]: Study Type'
    assert add_filter(rows,columns,filter) == [{'column-0': 'Observational [Patient Registry]: Study Type'}]


def test_add_filter_occupied_list():
    rows = [{'column-0': 'Observational [Patient Registry]: Study Type'}]
    filter = 'Interventional: Study Type'
    assert add_filter(rows, columns, filter) == [{'column-0': 'Observational [Patient Registry]: Study Type'},{'column-0': 'Interventional: Study Type'}]


def test_add_duplicate_filter():
    rows = [{'column-0': 'Observational [Patient Registry]: Study Type'}]
    filter = 'Observational [Patient Registry]: Study Type'
    assert add_filter(rows,columns,filter) == [{'column-0': 'Observational [Patient Registry]: Study Type'}]


def test_delete_filter_empty_list():
    rows = []
    selected_rows = [2]
    assert delete_filter(selected_rows,rows) == []


def test_delete_filter_one_in_list():
    rows = [{'column-0': 'Observational [Patient Registry]: Study Type'}]
    selected_rows = [0]
    assert  delete_filter(selected_rows,rows) == []


def test_delete_filter_two_in_list():
    rows = [{'column-0': 'Observational [Patient Registry]: Study Type'},{'column-0': 'Interventional: Study Type'}]
    selected_rows = [0]
    assert delete_filter(selected_rows, rows) == [{'column-0': 'Interventional: Study Type'}]


def test_delete_filter_middle_of_three():
    rows = [{'column-0': 'Observational: Study Type'}, {'column-0': 'Interventional: Study Type'}, {'column-0': 'Observational [Patient Registry]: Study Type'}]
    selected_rows = [1]
    assert delete_filter(selected_rows,rows) == [{'column-0': 'Observational: Study Type'}, {'column-0': 'Observational [Patient Registry]: Study Type'}]
