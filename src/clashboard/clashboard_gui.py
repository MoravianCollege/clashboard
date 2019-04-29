
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from clashboard.clinical_trials_data import ClinicalTrialsData
import plotly.graph_objs as go

study_type_counts = None
status_counts = None
phase_counts = None
count = 0
date = "4/27/2019"
clash = ClinicalTrialsData()
group_by = []
groups = clash.get_group_choices()

external_stylesheets = ['https://codepen.io/JPolich/pen/KYyRJG.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def setup_dropdown(groups):
    group_by = []
    for group in groups:
        curr_dict = {'label': group, 'value': group}
        group_by.append(curr_dict)
    return group_by


group_by = setup_dropdown(groups)
app.layout = html.Div(children=[
    html.H1(children='ClinicalTrails.gov Data Exploration'),

    dcc.Dropdown(
        options=[
            {'label': 'Bar Graph', 'value': 'bar_chart'},
            {'label': 'Pie Chart', 'value': 'pie_chart'}
        ],
        value='pie_chart',
        id='chart-type',
        style={'width': '200'}
    ),
    html.Div(
        dash_table.DataTable(
            id='adding-rows-table',
            columns=[{
                'name': 'Filters',
                'id': 'column-{}'.format(i),
                'deletable': False,
                'editable_name': False
            } for i in range(1)],
            data=[
                {'Column-{}'.format(i): (j + (i - 1) * 1) for i in range(1)}
                for j in range(0)
            ],
            row_deletable=False,
            row_selectable='single',

        ),
        style={'width': '30%',
               'display': 'inline-block',
               'vertical-align': 'top'},
    ),
    html.Div(
        dcc.Graph(
            id='my-graph'
        ),

        style={'width': '70%', 'display': 'inline-block', },
        id='plot-area'
    ),

    html.Div(
        html.Button('Delete Row', id='Delete-rows-button', n_clicks=0)
    ),

    dcc.Dropdown(
        options=group_by,
        value='phase',
        id='dropdown-id',
    ),
    html.H1(id='date', children='Data from ' + date),

    html.Div(id='intermediate-value', style={'display': 'none'})

])


@app.callback(
    [Output('adding-rows-table', 'data'),
     Output('intermediate-value', 'children')],
    [Input('my-graph', 'clickData'),
     Input('Delete-rows-button', 'n_clicks')],
    [State('adding-rows-table', 'data'),
     State('adding-rows-table', 'columns'),
     State('adding-rows-table', 'selected_rows'),
     State('chart-type', 'value')])
def on_click(click_data, n_clicks, rows, columns, selected_rows, chart_type):
    global count
    current_group_by = clash.get_group_by()
    curr_filter = get_filter(chart_type, click_data)
    if n_clicks > count:
        count += 1
        data = rows[selected_rows[0]]['column-0'].split(':')
        clash.remove_filter(str(data[0].strip()), str(data[1].strip()))
        return delete_filter(selected_rows, rows), " "

    else:
        clash.apply_filter(current_group_by, curr_filter)
        return add_filter(rows, columns,
                          (current_group_by + ": " + curr_filter)), " "


def get_filter(chart_type, click_data):
    if chart_type == 'pie_chart':
        return click_data.get("points")[0].get("label")
    elif chart_type == "bar_chart":
        return click_data.get("points")[0].get("x")
    else:
        return ""


def delete_filter(selected_rows, rows):
    if len(rows) > 0:
        for n in selected_rows:
            del rows[n]
    return rows


def add_filter(rows, columns, curr_filter):
    is_in = check_if_exists(rows, curr_filter)
    if not is_in:
        rows.append({c['id']: curr_filter for c in columns})
    return rows


def check_if_exists(rows, curr_filter):
    for row in rows:
        if row.get('column-0') == curr_filter:
            return True
    return False


@app.callback([Output('my-graph', 'figure'),
               Output('date', 'children')],
              [Input('dropdown-id', 'value'),
               Input('intermediate-value', "children"),
              Input('chart-type', 'value')])
def update_plot(value, n, chart_type):
    global date
    clash.set_group_by(value)
    labels = clash.get_labels()
    values = clash.get_values()
    date = 'Data from ' + clash.get_download_date()
    if chart_type == 'bar_chart':
        return go.Figure(
                data=[
                    go.Bar(x=labels, y=values)

                ],
                layout=go.Layout(
                    title=clash.get_group_by(),
                    showlegend=True,
                    margin=go.layout.Margin(r=0, t=40, b=30)
                )
            ), date
    elif chart_type == 'pie_chart':
        return go.Figure(
            data=[
                go.Pie(labels=labels, values=values)
            ],
            layout=go.Layout(
                title=clash.get_group_by(),
                showlegend=True,
                margin=go.layout.Margin(r=0, t=40, b=30)
            )
        ), date
    else:
        return {}, date


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
