import xml.etree.ElementTree as ET
import csv
from xml_to_csv_conversion.src.xmlElementInformation import xmlElementInformation

class xmlFieldInterpreter():

    def __init__(self, xmlFile):
        self.tree = ET.parse(xmlFile)
        self.root = self.tree.getroot()
        self.currentXMLInformation = xmlElementInformation
        self.tag_list = []
        self.text_list = []

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

    def get_all_keywords_or_conditions(self):
        currentXMLInformation = xmlElementInformation
        condition_list = []
        keyword_list = []
        elementFieldValues = []
        elementFieldTags = []
        elementFieldValues.append(self.getNCTid()[1])
        elementFieldTags.append(self.getNCTid()[0])
        for child in self.root:
            if not self.doesElementHaveChildren(child):
                if self.isChildDuplicateField(child):
                    if self.isDuplicateFieldCondition(child):
                        condition_list.append(child.text)
                    else:
                        keyword_list.append(child.text)
                else:
                    elementFieldTags.append(child.tag)
                    elementFieldValues.append(child.text)
        elementFieldTags.append("conditions")
        elementFieldTags.append("keywords")
        self.tag_list = elementFieldTags
        elementFieldValues.append(condition_list)
        elementFieldValues.append(keyword_list)
        self.text_list = elementFieldValues


    def isChildDuplicateField(self, currentElement):
        if currentElement.tag == "condition" or currentElement.tag == "keyword":
            return True
        else:
            return False

    def isDuplicateFieldCondition(self, currentElement):
        if currentElement.tag == "condition":
            return True
        else:
            return False

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

    def write_xml_element_tags_to_csv(self):
        # print(self.tag_list, "|||||_______________________|||||")
        if self.isCSVFileEmpty():
            with open('clinicalTrialData.csv', mode='w') as trial_data_file:
                trial_data_writer = csv.writer(trial_data_file, delimiter=',')
                trial_data_writer.writerow(self.tag_list)

    def write_xml_element_information_to_csv(self):
        print(self.text_list, "|||||_______________________|||||")
        if not self.isCSVFileEmpty():
            with open('clinicalTrialData.csv', mode='a') as trial_data_file:
                trial_data_writer = csv.writer(trial_data_file, delimiter=',')
                trial_data_writer.writerow(self.text_list)

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
