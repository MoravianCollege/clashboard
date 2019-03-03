from unittest import TestCase
import csv
import xml_to_csv_conversion.src.addSelectedNumberRowsToCSV as addSelected
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

    def test_zeroXMLFileAddedToCSVLine(self):
        self.overwriteDataFile()
        addSelected.AddSelectedDepthOneXMLValuesToCSV(0)
        self.assertTrue(self.countCSVFileLines() == 1)

    def test_oneXMLFileAddedToCSVLine(self):
        self.overwriteDataFile()
        addSelected.AddSelectedDepthOneXMLValuesToCSV(1)
        self.assertTrue(self.countCSVFileLines() == 2)

    def test_tenXMLFileAddedToCSVLine(self):
        self.overwriteDataFile()
        addSelected.AddSelectedDepthOneXMLValuesToCSV(10)
        self.assertEquals(11, self.countCSVFileLines())


