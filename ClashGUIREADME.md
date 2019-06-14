# Clashboard: clashboard_gui.py
*****
* **setup\_dropdown(self, groups)**
	* **groups**: A list of groups to be displayed
		*  Returns the list of options available in the dropdown display
		* Sets up the dropdown menu to be displayed
* **on\_click(click_data, n_clicks, group, rows, columns, selected_rows, chart_type)**
	* **click_data**: The point(s) on the graph in which the user clicked
	* **n_clicks**: Integer that represents the number of times a button has been clicked by the user
	* **group**: The current group being used to display data
	* **rows**: The list of the filters that have been applied by the user
	* **columns**: The list containing the identifiable columns (used by Dash)
	* **selected_rows**: The list of filters currently _selected_ by the user (from clicks)
	* **chart_type**: The type of visual graph to be displayed to the user
		*  Determines how to act when a user performs a click

* **get\_filter(chart_type, click_data)**
	* **chart_type**: The type of visual graph to be displayed to the user
	* **click_data**: The point(s) on the graph in which the user clicked
		*  Returns the filter the user wishes to view for the group currently being displayed
		* Used when the user clicks on a specific portion on the graph.=
* **delete\_filter(selected_rows, rows)**
	* **selected_rows**: The list of filters currently _selected_ by the user (from clicks)
	* **rows**:  The list of the filters that have been applied by the user
		*  Deletes a filter from the list of filters

* **add\_filter(rows, columns, curr_filter)**
	* **rows**:  The list of the filters that have been applied by the user
	* **columns**: The list containing the identifiable columns (used by Dash)
	* **curr_filter**: The current filter to be added to the list
		*  Adds a filter to the list of filters, if it does not already exist

* **check\_if\_exists(rows, curr_filter)**
	* **rows**:  The list of the filters that have been applied by the user
	* **curr_filter**: The current filter to be checked
		*  Checks if a filter has been added or chosen by the user already

* **get\_filters(rows)**
	* **rows**:  The list of the filters that have been applied by the user
		*  Returns a list containing tuples of the group name along with the filter name(s)
		* The list of filters contains all possible filters to be chosen by the user

* **update\_plot(group, chart_type, rows)**
	* **group**: The current group being used to display data
	* **chart_type**: The type of visual graph to be displayed to the user
	* **rows**: The list of the filters that have been applied by the user
		*  Updates elements of the display based on data received  
