# Clashboard Interface
-
* **replace\_underscore(self, filter\_category)**
	* **filter\_category**: The name of the filter to be altered
	* Removes all underscores from **filter\_category**, and replaces them with spaces.

* **replace\_space(self, filter\_category)**
 	* **filter\_category**: The name of the filter to be altered
	* Removes all spaces from **filter\_category**, and replaces them with underscores.

* **remove\_filter(self, filter\_category, filter\_name)**
	* **filter\_category**: The column in the database to be filtered
	* **filter\_name**: Specific value within specified column to filter on
	* Removes the filter with the specified category and name from the list of filters, and then reruns the database query.

* **apply\_filter(self, filter\_category, filter\_name)**
	* **filter\_category**: The column in the database to be filtered
	* **filter\_name**: Specific value within specified column to filter on
	* Adds a filter with the specified category and name to the list of filters, and then reruns the database query.

* **get\_current\_filters(self)**
	* Returns the list of currently applied filters as a list of human-readable strings.

* **set\_group\_by(self, attribute)**
	* **attribute**: A human-readable string
	* Converts **attribute** into its equivalent database value, and sets the data to be grouped by that attribute.
	
* **get\_group\_by(self)**
	* Returns the attribute the data is currently grouped by as a human-readable string.
 
* **get\_labels(self)**
	* Returns each category for grouping the data under the current attribute, as a list of human-readable strings.
 
* **get\_values(self)**
	* Returns a list of integers describing the frequency of each label for the current attribute.

* **update\_data(self, grouping)**
	* **grouping**: The current group-by to be used with the updated data
	* Re-queries the database, and updates the data available.