from unittest import TestCase
import csv
from xml_to_csv_conversion.src.getDepthOneFields import xmlFieldInterpreter
from xml_to_csv_conversion.src.xml_paths import *


class TestAddMultipleXMLToCSV(TestCase):
    main_xml_path = get_main_xml_directory_path()
    sub_directory_paths = get_sub_directory_paths_of_main_xml_path(main_xml_path)
    xml_file_paths = get_xml_file_paths_of_sub_directories(sub_directory_paths)

    def overwriteDataFile(self):
        file = open("clinicalTrialData.csv", mode='w')

    def countCSVFileLines(self):
        with open("clinicalTrialData.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            linecount = 0
            for row in csv_reader:
                linecount += 1
            return linecount

    def testGetAllXMLDirectories(self):
        self.assertIsInstance(xml_file_paths, list)
        self.assertTrue(len(xml_file_paths) != 0)

    def test_blankCSVFile(self):
        self.overwriteDataFile()
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        self.assertTrue(test_interpreter.isCSVFileEmpty())

    def test_tenXMLFilePathToCSVLine(self):
        self.overwriteDataFile()
        for i in range(0, 10, 1):
            test_interpreter = xmlFieldInterpreter(xml_file_paths[i])
            test_interpreter.writeFieldNamesWithIDToFile()
            test_interpreter.writeFieldValuesWithIDToFile()
        self.assertTrue(self.countCSVFileLines() == 11)

