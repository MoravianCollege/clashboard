import pandas as pd
import copy
from clashboard.clinical_database import gather_data


class ClinicalTrialsData:

    def __init__(self):
        self.type_counts = None
        self.curr_group = ''
        self.studies = pd.DataFrame()
        self.filters = []
        self.groupings = ['study_type', 'overall_status', 'phase',
                          'enrollment_type', 'last_known_status']

    def replace_underscore(self, filter_category):
        filter_category = filter_category.replace("_", " ").title()
        return filter_category

    def replace_space(self, filter_category):
        filter_category = filter_category.replace(" ", "_").lower()
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
            self.update_data(self.curr_group)
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
        self.update_data(self.curr_group)

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
        self.update_data(self.curr_group)

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
        if self.curr_group is self.studies.index.name:
            return list(self.studies.index)

        return []

    def get_values(self):
        """
        Get the list of integers describing the amounts for each label
        :return: an list of ints
        """
        if self.curr_group is self.studies.index.name:
            return list(self.studies.values)

        return []

    def get_group_choices(self):
        """
        bad name right now
        return list of human-readable strings
        """
        temp_groupings = []
        for group in self.groupings:
            if group != self.curr_group:
                temp_groupings.append(self.replace_underscore(group))
        return temp_groupings

    def update_data(self, grouping):
        self.studies = gather_data(grouping, self.filters)
