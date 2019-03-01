from unittest import TestCase
from xml_to_csv_conversion.src.createAllDepthOneCSVFile import depthOneCSVWriter

class addALLXMLDepthOneToCSV(TestCase):

    def AddAllDepthOneXMLValuesToCSV(self):
        csv_writer = depthOneCSVWriter
        depthOneCSVWriter.fill_depth_one_csv(csv_writer)
