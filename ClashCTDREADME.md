# Clashboard: ClinicalTrialsData
*****
* **replace\_underscore(self, filter\_category)**
	* **filter\_category**: The name of the filter to be altered
		* Removes all underscores from **filter\_category**, and replaces them with spaces, and capitalizes the first letter of each word.

* **replace\_space(self, filter\_category)**
 	* **filter\_category**: The name of the filter to be altered
		* Removes all spaces from **filter\_category**, and replaces them with underscores, and changes all letters to lowercase.

* **get\_group\_choices(self, group)**
 	* **group**: The current group to be used when the data is updated
		* Returns a list of possible groupings for use in GUI as human-readable strings
		* Does not include current group-by

* **get\_download\_date(self)**
	* Get the most recent download date for the data to be displayed.

* **update\_data(self, group, filters=[])**
	* **group**: The current group to be used when the data is updated
	* **filters**: The list of filters to be applied (if applicable)
		* Re-queries the database, and updates the data available.

* **compute\_results(self, group, filters=[])**
	* **group**: The current group to be used when the data is updated
	* **filters**: The list of filters to be applied (if applicable)
		* Returns the data to be displayed: a tuple containing a list of the values and a list of the labels.
		*  Computes the values for the data elements to be displayed and updated; handles the values, labels, and filters.
