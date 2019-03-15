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

	def __init__(self):
		load_dotenv()

		hostname = os.getenv('hostname')
		port = os.getenv('port')
		database = os.getenv('database')
		username = os.getenv('username')
		password = os.getenv('password')

		print('connecting to the AACT database')
		conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
		df = pd.read_sql('select * from studies', con=conn)
		print(df)

		#global study_type_counts
		#study_type_counts = df.groupby('study_type').size()
		#global status_counts
		#status_counts = df.groupby('overall_status').size()
		#global phase_counts
		#phase_counts = df.groupby('phase').size()

		print('connection successful')

	def remove_filter(self, filter):
		print()

	def apply_filter(self, filter):
		print()

	def get_current_filters(self):
		print()

	def set_group_by(self, attribute):
		print()

	def get_group_by(self):
		print()

	def get_labels(self):
		print()

	def get_values(self):
		print()

	def get_variables(self):
		print()


c = ClashInterface()
