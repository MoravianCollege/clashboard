import xml.etree.ElementTree as ET
import csv
from xml_to_csv_conversion.src.xmlElementInformation import xmlElementInformation


class xmlFieldInterpreter():

    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.currentXMLInformation = xmlElementInformation
        self.tag_list = []
        self.text_list = []
        self.condition_list = []
        self.keyword_list = []

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

    def doesElementHaveChildren(self, current_element):
        for child in current_element:
            return True
        else:
            return False

    def get_all_keywords_or_conditions(self):
        self.tag_list.append(self.getNCTid()[0])
        self.text_list.append(self.getNCTid()[1])
        for child in self.root:
            if not self.doesElementHaveChildren(child):
                self.accomodateDuplicateTags(child)

    def accomodateDuplicateTags(self, current_element):
        if self.isChildDuplicateField(current_element):
            if self.isDuplicateFieldCondition(current_element):
                self.condition_list.append(current_element.text)
            else:
                self.keyword_list.append(current_element.text)
        else:
            self.tag_list.append(current_element.tag)
            self.text_list.append(current_element.text)

    def addDuplicateValuesToValueList(self):
        self.tag_list.append("conditions")
        self.tag_list.append("keywords")
        self.text_list.append(self.condition_list)
        self.text_list.append(self.keyword_list)


    def isChildDuplicateField(self, current_element):
        if current_element.tag == "condition" or current_element.tag == "keyword":
            return True
        else:
            return False

    def isDuplicateFieldCondition(self, current_element):
        if current_element.tag == "condition":
            return True
        else:
            return False

    def write_xml_element_tags_to_csv(self):
        self.get_all_keywords_or_conditions()
        if self.isCSVFileEmpty():
            with open('clinicalTrialData.csv', mode='w') as trial_data_file:
                trial_data_writer = csv.writer(trial_data_file, delimiter=',')
                trial_data_writer.writerow(self.tag_list)

    def write_xml_element_information_to_csv(self):
        self.get_all_keywords_or_conditions()
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
