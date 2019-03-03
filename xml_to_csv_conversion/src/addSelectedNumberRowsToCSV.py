from xml_to_csv_conversion.src.getDepthOneFields import xmlFieldInterpreter
from xml_to_csv_conversion.src.xml_paths import *
csv_writer = xmlFieldInterpreter

main_xml_path = get_main_xml_directory_path()
sub_directory_paths = get_sub_directory_paths_of_main_xml_path(main_xml_path)
xml_file_paths = get_xml_file_paths_of_sub_directories(sub_directory_paths)


def AddSelectedDepthOneXMLValuesToCSV(number_of_xml_files):
    xmlInterpreter = xmlFieldInterpreter(xml_file_paths[0])
    xmlInterpreter.write_xml_element_tags_to_csv()
    if number_of_xml_files <= len(xml_file_paths) :
        for xml_file_path_index in range(0, number_of_xml_files, 1):
            xmlInterpreter = xmlFieldInterpreter(xml_file_paths[xml_file_path_index])
            xmlInterpreter.write_xml_element_information_to_csv()


def overwriteDataFile():
    file = open("clinicalTrialData.csv", mode='w')
