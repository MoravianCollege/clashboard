from xml_to_csv_conversion.src.getDepthOneFields import xmlFieldInterpreter
from xml_to_csv_conversion.src.largestXMLTagGroup import largestXMLTagGroup
from xml_to_csv_conversion.src.missingXMLValueCreator import missingXMLValueCreator
from xml_to_csv_conversion.src.xml_paths import *
xml_to_csv_tag_writer = largestXMLTagGroup()


file = open("clinicalTrialData.csv", mode='w')

main_xml_path = get_main_xml_directory_path()
sub_directory_paths = get_sub_directory_paths_of_main_xml_path(main_xml_path)
xml_file_paths = get_xml_file_paths_of_sub_directories(sub_directory_paths)


def AddAllDepthOneXMLValuesToCSV():
    DetermineXMLTagList()
    for xml_file_path_index in range(0, len(xml_file_paths), 1):
        xml_interpreter = xmlFieldInterpreter(xml_file_paths[xml_file_path_index])
        DetermineXMLValueList(xml_interpreter)
        print("Text:", xml_file_path_index)

def DetermineXMLValueList(xml_interpreter):
    xml_interpreter.getAllKeywordsOrConditions()
    missingXMLValueCreator(xml_interpreter.text_list, xml_interpreter.tag_list, xml_to_csv_tag_writer.longest_tag_list)

def DetermineXMLTagList():
    for xml_file_path_index in range(0, len(xml_file_paths), 1):
        print("Tags:", xml_file_path_index)
        xml_interpreter = xmlFieldInterpreter(xml_file_paths[xml_file_path_index])
        xml_to_csv_tag_writer.ensureLargestTagList(xml_interpreter.root)


AddAllDepthOneXMLValuesToCSV()
