from xml_to_csv_conversion.src.xml_paths import *
import os

xml_to_csv_conversion_path = os.path.dirname(os.getcwd())
clashboard_path = os.path.dirname(xml_to_csv_conversion_path)
destination_path = os.path.dirname(clashboard_path)


def test_all_public_xml_directory_not_in_correct_location():
    assert is_main_xml_directory_in_correct_location()


def test_find_xml_folder_path():
    assert main_xml_path.split("/")[-1] == "AllPublicXML"


def test_find_sub_directory_paths():
    assert len(sub_directory_paths) == len(os.listdir(get_main_xml_directory_path())) - 2


def test_find_xml_file_paths():
    count = 0
    for sub_directory_path in sub_directory_paths:
        count += len(os.listdir(sub_directory_path))
    assert len(xml_file_paths) == count
