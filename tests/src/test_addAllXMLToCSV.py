from unittest import TestCase
from xml_to_csv_conversion.src.createDepthOneCSVFile import depthOneCSVWriter

class test_addALLXMLToCSV(TestCase):

    def test_AddAllDepthOneXMLValuesToCSV(self):
        csv_writer = depthOneCSVWriter
        depthOneCSVWriter.fill_depth_one_csv(csv_writer)
