import csv
import pandas as pd


class MockDB:

    phases = {'N/A': 0, 'Phase 2': 0, 'Phase 3': 0, 'Phase 4': 0}
    studies = None
    file = None

    def __init__(self, filename):
        self.file = filename

    def populate_tables(self):
        with open(self.file) as file:
            trial_data = csv.reader(file, delimiter=',')
            for row in trial_data:
                phase = row[38]
                print(phase)
                if phase == 'phase' or phase == '':
                    pass
                else:
                    self.phases[phase] += 1
        self.studies = pd.DataFrame(self.phases)

    def groupby(self, attribute):
        pass

    def size(self):
        pass
