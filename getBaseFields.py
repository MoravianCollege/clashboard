import xml.etree.ElementTree as ET
import csv


class xmlFieldInterpreter():

    def __init__(self, xmlFile):
        self.tree = ET.parse(xmlFile)
        self.root = self.tree.getroot()

    def getNCTid(self):
        for child in self.root:
            if child.tag == "id_info":
                for grand_child in child:
                    if grand_child.tag == "nct_id":
                        return [grand_child.tag, grand_child.text]

    def getTopLevelFieldsTags(self):
        top_fields = []
        for child in self.root:
            top_fields.append(child.tag)
        return top_fields

    def getFieldsWithID(self):
        id_info_pair = [self.getNCTid(), self.getTopLevelFieldsTags()]
        return id_info_pair

    def doesElementHaveChildren(self, currentElement):
        for child in currentElement:
            return True
        else:
            return False

    def getBaseFieldTags(self):
        elementFieldTags = []
        elementFieldTags.append(self.getNCTid()[0])
        for child in self.root:
            if not self.doesElementHaveChildren(child):
                elementFieldTags.append(child.tag)
        return elementFieldTags

    def getBaseFieldValues(self):
        elementFieldValues = []
        elementFieldValues.append(self.getNCTid()[1])
        for child in self.root:
            if not self.doesElementHaveChildren(child):
                elementFieldValues.append(child.text)
        return elementFieldValues
    
    def writeFieldNamesWithIDToFile(self):
        if self.isCSVFileEmpty():
            with open('clinicalTrialData.csv', mode='w') as trial_data_file:
                trial_data_writer = csv.writer(trial_data_file, delimiter=',')
                trial_data_writer.writerow(self.getBaseFieldTags())

    def writeFieldValuesWithIDToFile(self):
        if not self.isCSVFileEmpty():
            with open('clinicalTrialData.csv', mode='a') as trial_data_file:
                trial_data_writer = csv.writer(trial_data_file, delimiter=',')
                trial_data_writer.writerow(self.getBaseFieldValues())

    def isCSVFileEmpty(self):
        try:
            with open("clinicalTrialData.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                linecount = 0
                for row in csv_reader:
                    if not row == []:
                        linecount += 1
                return linecount == 0
        except IOError:
            file = open("clinicalTrialData.csv", mode='w')
            return True
