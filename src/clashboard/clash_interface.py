from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd


class ClashInterface:

	conn = None
	data_table = None
	value_counts = None
	group_by = None
	filters = []

	def __init__(self):
		load_dotenv()

		hostname = os.getenv('hostname')
		database = os.getenv('database')
		username = os.getenv('username')
		password = os.getenv('password')

		print('connecting to the AACT database')
		conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
		global data_table
		data_table = pd.read_sql('select * from studies', con=conn)
		print('connection successful')

	def remove_filter(self, filter):
		self.filters.remove(filter)

	def apply_filter(self, filter):
		self.filters.append(filter)

	def get_current_filters(self):
		return self.filters

	def set_group_by(self, attribute):
		global data_table
		global value_counts
		value_counts = data_table.groupby(attribute).size()
		global group_by
		group_by = attribute

	def get_group_by(self):
		global group_by
		return group_by

	def get_labels(self):
		global value_counts
		return value_counts.index

	def get_values(self):
		global value_counts
		return value_counts.values

	def get_variables(self):
		print()


c = ClashInterface()
c.set_group_by("overall_status")
c.apply_filter("phase")
c.apply_filter("enrollment")
print(c.get_current_filters())
c.remove_filter("phase")
print(c.get_current_filters())
