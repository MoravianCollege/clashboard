from unittest import TestCase
import csv
from xml_to_csv_conversion.src.getDepthOneFields import xmlFieldInterpreter


class TestXmlDepthOneSingleFileInterpreter(TestCase):

    def overwriteDataFile(self):
        file = open("clinicalTrialData.csv", mode='w')

    def countCSVFileLines(self):
        with open("clinicalTrialData.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            linecount = 0
            for row in csv_reader:
                linecount += 1
            return linecount

    def test_makeXMLFieldInterpreter(self):
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")

    def test_getNCTID(self):
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        nct_id = test_interpreter.getNCTid()
        self.assertIsNotNone(nct_id)
        self.assertIsInstance(nct_id[0], str)

    def test_getDifferentNCTID(self):
        first_test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        first_nct_id = first_test_interpreter.getNCTid()
        second_test_interpreter = xmlFieldInterpreter("NCT00001308.xml")
        second_nct_id = second_test_interpreter.getNCTid()
        self.assertIsNot(first_nct_id, second_nct_id)

    def test_blankCSVFile(self):
        self.overwriteDataFile()
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        self.assertTrue(test_interpreter.isCSVFileEmpty())

    def test_addBaseFieldsToCSV(self):
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        self.overwriteDataFile()
        test_interpreter.write_xml_element_tags_to_csv()
        self.assertFalse(test_interpreter.isCSVFileEmpty())
        self.assertEqual(1, self.countCSVFileLines())

    def test_addingFieldNamesTwice(self):
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        self.overwriteDataFile()
        test_interpreter.write_xml_element_tags_to_csv()
        test_interpreter.write_xml_element_tags_to_csv()
        self.assertFalse(test_interpreter.isCSVFileEmpty())
        self.assertEqual(1, self.countCSVFileLines())

    def test_addFieldValuesToCSV(self):
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        self.overwriteDataFile()
        test_interpreter.write_xml_element_tags_to_csv()
        test_interpreter.write_xml_element_information_to_csv()
        self.assertFalse(test_interpreter.isCSVFileEmpty())
        self.assertEqual(2, self.countCSVFileLines())

    def test_multipleFieldValuesAdded(self):
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        self.overwriteDataFile()
        test_interpreter.write_xml_element_tags_to_csv()
        test_interpreter.write_xml_element_information_to_csv()
        test_interpreter = xmlFieldInterpreter("NCT00001308.xml")
        test_interpreter.write_xml_element_information_to_csv()
        self.assertFalse(test_interpreter.isCSVFileEmpty())
        self.assertEqual(3, self.countCSVFileLines())


