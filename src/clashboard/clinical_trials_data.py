import copy
from clashboard.clinical_database import ClinicalDataCollector


class ClinicalTrialsData:

    def __init__(self):
        self.cdc = ClinicalDataCollector()
        self.groupings = ['study_type', 'overall_status', 'phase',
                          'enrollment_type', 'last_known_status']

    def replace_underscore(self, filter_category):
        filter_category = filter_category.replace("_", " ").title()
        return filter_category

    def replace_space(self, filter_category):
        filter_category = filter_category.replace(" ", "_").lower()
        return filter_category

    def get_group_choices(self, group):
        """
        Gets the potential choices for grouping the data
        :return: list of human-readable potential groupings
        """
        temp_groupings = self.groupings.copy()

        if group in self.groupings:
            temp_groupings.remove(group)

        temp_groupings = list(map(self.replace_underscore, temp_groupings))

        return temp_groupings

    def get_download_date(self):
        """
        Gets the most recent download date for the data
        :return: string that represents the date
        """
        download_date = self.cdc.get_most_recent_date()
        return "{}/{}/{}".format(download_date.month,
                                 download_date.day,
                                 download_date.year)

    def update_data(self, group, filters=[]):
        if group not in self.groupings:
            return [], []
        values, labels = [], []
        data = self.cdc.gather_data(group, filters)

        if group == data.index.name:
            values = list(data.values)
            labels = list(data.index)
        else:
            return [], []

        return labels, values

    def compute_results(self, group, filters=[]):
        group = self.replace_space(group)
        if group not in self.groupings:
            return [], []
        filters = [(self.replace_space(value[0]),
                    value[1]) for value in filters]
        data = self.update_data(group, filters)

        return data
