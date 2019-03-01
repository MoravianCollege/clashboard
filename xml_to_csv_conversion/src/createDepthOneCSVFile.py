from xml_to_csv_conversion.src.getBaseFields import xmlFieldInterpreter
from xml_to_csv_conversion.src.xml_paths import *


class depthOneCSVWriter():

    def __init__(self):
        self.main_xml_path = get_main_xml_directory_path()
        self.sub_directory_paths = get_sub_directory_paths_of_main_xml_path(main_xml_path)
        self.xml_file_paths = get_xml_file_paths_of_sub_directories(sub_directory_paths)
        self.xmlInterpreter = xmlFieldInterpreter(xml_file_paths[0])
        self.xmlInterpreter.writeFieldNamesWithIDToFile()

    def fill_depth_one_csv(self):
        for xml_file_path_index in range(0, len(xml_file_paths), 1):
            self.xmlInterpreter = xmlFieldInterpreter(xml_file_paths[xml_file_path_index])
            self.xmlInterpreter.writeFieldValuesWithIDToFile()
