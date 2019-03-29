
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from clashboard.clinical_trials_data import ClinicalTrialsData as CTD

study_type_counts = None
status_counts = None
phase_counts = None
currentGroupBy = None
count = 0


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
   html.H1(children='ClinicalTrails.gov Data Exploration'),

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
           row_selectable='multi',
       ),

       style={'width': '30%', 'display': 'inline-block', 'vertical-align': 'top'},


   ),


   html.Div(
       dcc.Graph(
           id='my-graph'
       ),

       style={'width': '70%', 'display': 'inline-block',},
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
       id='dropdown-id'
   ),



   html.Div(id='click-data'),
])


@app.callback(
   Output('adding-rows-table', 'data'),
   [Input('my-graph', 'clickData'),
    Input('Delete-rows-button', 'n_clicks'),
    Input('adding-rows-table', 'selected_rows')],
   [State('adding-rows-table', 'data'),
    State('adding-rows-table', 'columns')])
def get_filter(click_data, n_clicks, selected_rows, rows, columns):
    global count
    filter = (click_data.get("points")[0].get("label") + ": " + currentGroupBy)
    is_in = check_if_exists(rows, filter)

    if n_clicks > count:
        count += 1
        print("hello delete")

        for n in selected_rows:
            print(rows[n])
            del rows[n]
        return rows
    else:
        if not is_in:
            rows.append({c['id']: filter for c in columns})
            return rows
        else:
            return rows


def check_if_exists(rows, filter):
    for row in rows:
        if row.get('column-0') == filter:
            return True
    return False


@app.callback(Output('my-graph', 'figure'),
             [Input('dropdown-id', 'value')])
def update_plot(value):
    global currentGroupBy
    if value == 'study_type':
        labels = study_type_counts.index
        values = study_type_counts.values
        title = 'Study Type'
    elif value == 'overall_status':
        labels = status_counts.index
        values = status_counts.values
        title = 'Status'
    elif value == 'phase':
        labels = phase_counts.index
        values = phase_counts.values
        title = 'Phase'
    else:
        labels = []
        values = []
        title = ''

    currentGroupBy = title

    return go.Figure(
           data=[
               go.Pie(labels=labels, values=values)
           ],
           layout=go.Layout(
               title=title,
               showlegend=True,
               margin=go.layout.Margin(l=40, r=0, t=40, b=30)
           )
       )


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')

