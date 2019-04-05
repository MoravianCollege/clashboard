import pandas as pd
import copy
from clashboard.clinical_database import ClinicalTrialsQuery


class ClinicalTrialsData:

    def __init__(self):
        self.type_counts = None
        self.curr_group = ''
        self.studies = pd.DataFrame()
        self.filters = []
        self.ctq = ClinicalTrialsQuery()

    def replace_underscore(self, filter_category):
        filter_category = filter_category.replace("_", " ")
        return filter_category

    def replace_space(self, filter_category):
        filter_category = filter_category.replace(" ", "_")
        return filter_category

    def remove_filter(self, filter_category, filter_name):
        """
        Removes a specified filter from the list of filters,
           and re-runs the query
        :param filter_category:
               the column in the DB that the user wants to filter
        :param filter_name:
               the specific value to filter on in that column
        """
        filter_category = self.replace_space(filter_category)
        try:
            self.filters.remove([filter_category, filter_name])
        except ValueError:
            pass

    def apply_filter(self, filter_category, filter_name):
        """
        Adds the specified filter to the list of filters,
           and re-runs the current query
        :param filter_category:
               the column in the DB that the user wants to filter
        :param filter_name:
               the specific value to filter on in that column
        """
        filter_category = self.replace_space(filter_category)
        self.filters.append([filter_category, filter_name])

    def get_current_filters(self):
        """
        Get the list of currently applied filters
        :return: the list of human-readable strings
        """
        new_filters = copy.deepcopy(self.filters)
        for x in new_filters:
            x[0] = self.replace_underscore(x[0])
        return new_filters

    def set_group_by(self, attribute):
        """
        Sets the attribute to group the data by
        :param attribute:
               human-readable string
        """
        self.curr_group = self.replace_space(attribute)

    def get_group_by(self):
        """
        Get the variable currently used to group the data
        :return: a human-readable string
        """
        return self.replace_underscore(self.curr_group)

    def get_labels(self):
        """
        Get the lists of strings describing each category
           for grouping the data
        :return:
               list of human-readable strings
        """
        if self.curr_group in self.studies:
            labels = self.studies.groupby(self.curr_group).size().index
            # labels = self.studies.size().index
            return list(labels)

        return []

    def get_values(self):
        """
        Get the list of integers describing the amounts for each label
        :return: an list of ints
        """
        if self.curr_group in self.studies:
            values = self.studies.groupby(self.curr_group).size().values
            # values = self.studies.size().values
            return list(values)

        return []

    # Uncomment when tested and implemented
    # def get_variables(self):
    #    """
    #    Get the variables describing the options for displaying data
    #    :return:
    #           a list of dictionaries containing
    #           the label for human-readable display
    #           and the corresponding string in terms
    #           of the XML Schema
    #    ex - {'label': 'Study Type', 'value': 'study_type'}
    #         {'Study Type': 'study_type'}
    #    """
    #    pass

    def populate_tables(self):
        self.studies = self.ctq.db_query()
