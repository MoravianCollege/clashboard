
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
currentGroupBy = None
count = 0
clash = ClinicalTrialsData()
Date = '04/05/2019'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
        style={'width': '30%', 'display': 'inline-block', 'vertical-align': 'top'},
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
        options=[
            {'label': 'Study Type', 'value': 'study_type'},
            {'label': 'Status', 'value': 'overall_status'},
            {'label': 'Phase', 'value': 'phase'}
        ],
        value='study_type',
        id='dropdown-id',
    ),
    html.H1(children='Data from ' + Date),

])


@app.callback(
    Output('adding-rows-table', 'data'),
    [Input('my-graph', 'clickData'),
     Input('Delete-rows-button', 'n_clicks')],
    [State('adding-rows-table', 'data'),
     State('adding-rows-table', 'columns'),
     State('adding-rows-table', 'selected_rows'),
     State('chart-type', 'value')])
def on_click(click_data, n_clicks, rows, columns, selected_rows, chart_type):
    global count
    curr_filter = get_filter(chart_type, click_data)
    if n_clicks > count:
        count += 1
        clash.remove_filter(currentGroupBy, curr_filter)
        return delete_filter(selected_rows, rows)
    else:
        clash.apply_filter(currentGroupBy, curr_filter)
        return add_filter(rows, columns, (currentGroupBy + ": " + curr_filter))


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


@app.callback(Output('my-graph', 'figure'),
              [Input('dropdown-id', 'value'),
              Input('chart-type', 'value')])
def update_plot(value, chart_type):
    global currentGroupBy
    clash.set_group_by(value)
    labels = clash.get_labels()
    values = clash.get_values()
    currentGroupBy = value
    if chart_type == 'bar_chart':
        return go.Figure(
                data=[
                    go.Bar(x=labels, y=values)

                ],
                layout=go.Layout(
                    title=currentGroupBy,
                    showlegend=True,
                    margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                )
            )
    elif chart_type == 'pie_chart':
        return go.Figure(
            data=[
                go.Pie(labels=labels, values=values)
            ],
            layout=go.Layout(
                title=currentGroupBy,
                showlegend=True,
                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
            )
        )


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')