# Clashboard: ClinicalDataCollector
*****

* **gather\_data(self, group='', filters=None)**
	* **group**: The group to collect data on, if applicable
	* **filters**: The list of filters to collect data on, if applicable
		* Returns new data if any new filters or groups have been altered
		* Requeries if applicable

* **query\_data(self, filters=[])**
	* **filters**: The list of filters to retrieve data from, if applicable
		* Returns an SQL command
		* Uses SQL to fetch and receive data, will create a query

* **create\_query(self, filters=[])**
	* **filters**: The list of filters to retrieve data from, if applicable
		* Returns an SQL command
		* Uses SQL to create the query to be used

* **build\_filters\_query(self, filters=[])**
	* **filters**: The list of filters to retrieve data from, if applicable
		* Returns the list of filters in a format for SQL to read/translate from

* **make\_local\_table(self, table, local=False)**
	* **table**: The name of the table to retrieve data from in the database
	* **local**: A boolean indicating whether or not the database exists on the local machine
		* Creates a local table based on the study desired by the user
		* Needed in order to create a query

* **make\_connection(self)**
	* Allows a connection to be made between SQL (database) and the program

* **fetch\_sql\_data(self, sql_command)**
	* **sql_command**: The SQL command needed in order to create the query
		* Returns a Data Frame created after reading
		* Uses an SQL query and reads it in order to produce the data

* **get\_group\_data(self, sql_command, group='')**
	* **sql_command**: The SQL command needed in order to create the query
	* **group**: The group to collect data on, if applicable
		* Returns a Data Frame object (from Pandas)
		* Sorts data by splitting the object and combining the results into the Data Frame

* **get\_most\_recent\_date(self)**
	* Retrieves the last date that the acquired data has been updated
