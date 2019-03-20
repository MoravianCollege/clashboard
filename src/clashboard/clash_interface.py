from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

class clash_interface:

	conn = None
	df = None
	#study_type_counts = None
	#status_counts = None
	#phase_counts = None

	def __init__(self):
		load_dotenv()

		hostname = os.getenv('hostname')
		port = os.getenv('port')
		database = os.getenv('database')
		username = os.getenv('username')
		password = os.getenv('password')

	def remove_filter(filter):

	def apply_filter(filter):

	def get_current_filters():

	def set_group_by(attribute):

	def get_group_by():

	def get_labels():

	def get_values():

	def get_variables():