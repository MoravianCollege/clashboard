import pandas as pd



class ClinicalTrialsQuery:
    def __init__(self):
        sql_command = ''
        trials_data = pd.DataFrame()
        is_called = False


    def db_query(self, filters = [], group = ''):
        """
        New SQL QUERY
        :param filters:
        :param groupby:
        :return:
        """
        self.sql_command = "SELECT * FROM ctgov.studies"
        self.is_called = True
        return self.trials_data


    def update_data(self, group = ''):
        """
        Update GROUP BY
        :param groupby:
        :return:
        """
        return self.trials_data.groupby([group]) if self.is_called else None
