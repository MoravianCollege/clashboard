import csv


class largestXMLTagGroup():
    def __init__(self):
        self.longest_tag_list = []
        self.current_tag_list = []

    def ensureLargestTagList(self, current_element):
        self.getAllUniqueTags(current_element)
        self.isNewTagListLarger()
        self.write_xml_element_tags_to_csv()

    def isNewTagListLarger(self):
        if len(self.current_tag_list) > len(self.longest_tag_list):
            self.longest_tag_list = self.current_tag_list
            self.overwriteDataFile()

    def doesElementHaveChildren(self, current_element):
        for child in current_element:
            return True
        else:
            return False

    def getAllUniqueTags(self, current_element):
        self.current_tag_list = []
        self.current_tag_list.append(self.getNCTid(current_element))
        for child in current_element:
            if not self.doesElementHaveChildren(child):
                self.accomodateDuplicateTags(child)
        self.current_tag_list.append("conditions")
        self.current_tag_list.append("keywords")

    def accomodateDuplicateTags(self, current_element):
        if not self.isChildDuplicateField(current_element):
            self.current_tag_list.append(current_element.tag)

    def isChildDuplicateField(self, current_element):
        if current_element.tag == "condition" or current_element.tag == "keyword":
            return True
        else:
            return False

    def getNCTid(self, current_element):
        for child in current_element:
            if child.tag == "id_info":
                for grand_child in child:
                    if grand_child.tag == "nct_id":
                        return grand_child.tag

    def write_xml_element_tags_to_csv(self):
        if self.isCSVFileEmpty():
            with open('clinicalTrialData.csv', mode='w') as trial_data_file:
                trial_data_writer = csv.writer(trial_data_file, delimiter=',')
                trial_data_writer.writerow(self.longest_tag_list)

    def isCSVFileEmpty(self):
        try:
            with open("clinicalTrialData.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                return self.countCSVRows(csv_reader) == 0
        except IOError:
            file = open("clinicalTrialData.csv", mode='w')
            file.close()
            return True

    def countCSVRows(self, csv_reader):
        line_count = 0
        for row in csv_reader:
            if not row == []:
                line_count += 1
        return line_count

    def overwriteDataFile(self):
        file = open("clinicalTrialData.csv", mode='w')
