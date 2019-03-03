from xml_to_csv_conversion.src.getDepthOneFields import xmlFieldInterpreter
from xml_to_csv_conversion.src.xml_paths import *


file = open("clinicalTrialData.csv", mode='w')

main_xml_path = get_main_xml_directory_path()
sub_directory_paths = get_sub_directory_paths_of_main_xml_path(main_xml_path)
xml_file_paths = get_xml_file_paths_of_sub_directories(sub_directory_paths)

def fill_depth_one_csv():
    xmlInterpreter = xmlFieldInterpreter(xml_file_paths[0])
    xmlInterpreter.write_xml_element_tags_to_csv()
    for xml_file_path_index in range(0, len(xml_file_paths), 1):
        xmlInterpreter = xmlFieldInterpreter(xml_file_paths[xml_file_path_index])
        xmlInterpreter.write_xml_element_information_to_csv()


fill_depth_one_csv()
