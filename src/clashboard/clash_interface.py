from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go


class ClashInterface:
    conn = None
    df = None

    # study_type_counts = None
    # status_counts = None
    # phase_counts = None

    def __init__(self):
        load_dotenv()

        hostname = os.getenv('hostname')
        port = os.getenv('port')
        database = os.getenv('database')
        username = os.getenv('username')
        password = os.getenv('password')

    def remove_filter(self, filter):
        pass

    def apply_filter(self, filter):
        pass

    def get_current_filters(self):
        pass

    def set_group_by(self, attribute):
        pass

    def get_group_by(self):
        return []

    def get_labels(self):
        pass

    def get_values(self):
        pass

    def get_variables(self):
        pass
