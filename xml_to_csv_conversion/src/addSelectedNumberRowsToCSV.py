from xml_to_csv_conversion.src.getDepthOneFields import xmlFieldInterpreter
from xml_to_csv_conversion.src.largestXMLTagGroup import largestXMLTagGroup
from xml_to_csv_conversion.src.missingXMLValueCreator import missingXMLValueCreator
from xml_to_csv_conversion.src.xml_paths import *
csv_writer = xmlFieldInterpreter
xml_to_csv_tag_writer = largestXMLTagGroup()

main_xml_path = get_main_xml_directory_path()
sub_directory_paths = get_sub_directory_paths_of_main_xml_path(main_xml_path)
xml_file_paths = get_xml_file_paths_of_sub_directories(sub_directory_paths)


def AddSelectedDepthOneXMLValuesToCSV(number_of_xml_files):
    DetermineXMLTagList(number_of_xml_files)
    if number_of_xml_files <= len(xml_file_paths):
        for xml_file_path_index in range(0, number_of_xml_files, 1):
            xml_interpreter = xmlFieldInterpreter(xml_file_paths[xml_file_path_index])
            DetermineXMLValueList(xml_interpreter)

def DetermineXMLValueList(xml_interpreter):
    xml_interpreter.getAllKeywordsOrConditions()
    missingXMLValueCreator(xml_interpreter.text_list, xml_interpreter.tag_list, xml_to_csv_tag_writer.longest_tag_list)

def DetermineXMLTagList(number_of_xml_files):
    if number_of_xml_files <= len(xml_file_paths):
        for xml_file_path_index in range(0, number_of_xml_files, 1):
            xml_interpreter = xmlFieldInterpreter(xml_file_paths[xml_file_path_index])
            xml_to_csv_tag_writer.ensureLargestTagList(xml_interpreter.root)

