import os


xml_to_csv_conversion_path = os.path.dirname(os.getcwd())
clashboard_path = os.path.dirname(xml_to_csv_conversion_path)
destination_path = os.path.dirname(clashboard_path)


def is_main_xml_directory_in_correct_location():
    if "AllPublicXML" not in os.listdir(destination_path):
        return False
    else:
        return True


def get_main_xml_directory_path():
    if is_main_xml_directory_in_correct_location():
        for item in os.listdir(destination_path):
            if item == "AllPublicXML":
                return os.path.join(destination_path, item)


def get_sub_directory_paths_of_main_xml_path(main_xml_path):
    sub_directory_paths = []

    for sub_directory in os.listdir(main_xml_path):
        sub_directory_paths.append(os.path.join(main_xml_path, sub_directory))
    for sub_directory_path in sub_directory_paths:
        if sub_directory_path.__contains__("Contents.txt") or sub_directory_path.__contains__(".DS_Store"):
            sub_directory_paths.remove(sub_directory_path)
    return sub_directory_paths


def get_xml_file_paths_of_sub_directories(sub_directory_paths):
    xml_file_paths = []
    for sub_directory_path in sub_directory_paths:
        for xml_file_name in os.listdir(sub_directory_path):
            xml_file_paths.append(os.path.join(sub_directory_path, xml_file_name))
    return xml_file_paths


main_xml_path = get_main_xml_directory_path()
sub_directory_paths = get_sub_directory_paths_of_main_xml_path(main_xml_path)
xml_file_paths = get_xml_file_paths_of_sub_directories(sub_directory_paths)