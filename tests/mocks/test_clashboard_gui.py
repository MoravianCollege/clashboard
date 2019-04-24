from clashboard.clashboard_gui import add_filter, delete_filter, get_filter,check_if_exists, setup_dropdown

columns = [{'name': 'Filters', 'id': 'column-0', 'deletable': False, 'editable_name': False}]


def test_add_filter_empty_list():
    rows = []
    filter = 'Observational [Patient Registry]: Study Type'
    assert add_filter(rows, columns, filter) == [{'column-0': 'Observational [Patient Registry]: Study Type'}]


def test_add_filter_occupied_list():
    rows = [{'column-0': 'Observational [Patient Registry]: Study Type'}]
    filter = 'Interventional: Study Type'
    assert add_filter(rows, columns, filter) == [{'column-0': 'Observational [Patient Registry]: Study Type'},
                                                 {'column-0': 'Interventional: Study Type'}]


def test_add_duplicate_filter():
    rows = [{'column-0': 'Observational [Patient Registry]: Study Type'}]
    filter = 'Observational [Patient Registry]: Study Type'
    assert add_filter(rows, columns, filter) == [{'column-0': 'Observational [Patient Registry]: Study Type'}]


def test_delete_filter_empty_list():
    rows = []
    selected_rows = [2]
    assert delete_filter(selected_rows, rows) == []


def test_delete_filter_one_in_list():
    rows = [{'column-0': 'Observational [Patient Registry]: Study Type'}]
    selected_rows = [0]
    assert delete_filter(selected_rows, rows) == []


def test_delete_filter_two_in_list():
    rows = [{'column-0': 'Observational [Patient Registry]: Study Type'}, {'column-0': 'Interventional: Study Type'}]
    selected_rows = [0]
    assert delete_filter(selected_rows, rows) == [{'column-0': 'Interventional: Study Type'}]


def test_delete_filter_middle_of_three():
    rows = [{'column-0': 'Observational: Study Type'}, {'column-0': 'Interventional: Study Type'},
            {'column-0': 'Observational [Patient Registry]: Study Type'}]
    selected_rows = [1]
    assert delete_filter(selected_rows, rows) == [{'column-0': 'Observational: Study Type'},
                                                  {'column-0': 'Observational [Patient Registry]: Study Type'}]


def test_get_filter_pie_chart():
    chart_type = "pie_chart"
    click_data = {'points': [{'curveNumber': 0, 'label': 'Observational', 'color': '#ff7f0e',
                              'value': 56725, 'percent': 0.1877733015991764, 'v': 56725, 'i': 3, 'pointNumber': 3,
                              'pointNumbers': [3]}]}
    assert get_filter(chart_type, click_data) == 'Observational'


def test_get_filter_bar_graph():
    chart_type = "bar_chart"
    click_data = {'points': [{'curveNumber': 0, 'pointNumber': 1, 'pointIndex': 1, 'x': 'Interventional',
                              'y': 239276}]}
    assert get_filter(chart_type, click_data) == 'Interventional'


def test_if_in_is_in():
    rows = [{'column-0': 'Observational [Patient Registry]: Study Type'},
            {'column-0': 'Interventional: Study Type'}]
    assert check_if_exists(rows, "Interventional: Study Type")


def test_if_in_not_in():
    rows = [{'column-0': 'Observational [Patient Registry]: Study Type'}]
    assert not check_if_exists(rows, "Interventional: Study Type")


def test_dropdown_setup():
    groups = ["Study Type", "Overall Status", "Phase", "Enrollment Type", "Overall Status"]
    group_by = setup_dropdown(groups)
    print("group_by:" + str(group_by))
    assert group_by == [{'label': 'Study Type', 'value': 'Study Type'},
                        {'label': 'Overall Status', 'value': 'Overall Status'},
                        {'label': 'Phase', 'value': 'Phase'},
                        {'label': 'Enrollment Type', 'value': 'Enrollment Type'},
                        {'label': 'Overall Status', 'value': 'Overall Status'}]