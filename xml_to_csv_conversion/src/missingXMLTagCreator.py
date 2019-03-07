import csv


def missingXMLTagCreator(current_text_list, current_tag_list, overall_tag_list):
    current_tag_iterator = 0
    while current_tag_iterator < len(overall_tag_list):
        if isXMLTagMissing(current_tag_list, overall_tag_list[current_tag_iterator]):
            if current_tag_iterator < len(current_text_list):
                current_text_list.insert(current_tag_iterator, "N/A")
            else:
                current_text_list.append("N/A")
        current_tag_iterator += 1
    write_xml_element_information_to_csv(current_text_list)

def isXMLTagMissing(current_tag_list, current_overall_tag):
    if current_overall_tag in current_tag_list:
        return False
    else:
        return True

def write_xml_element_information_to_csv(text_value_list):
    if not isCSVFileEmpty():
        with open('clinicalTrialData.csv', mode='a') as trial_data_file:
            trial_data_writer = csv.writer(trial_data_file, delimiter=',')
            trial_data_writer.writerow(text_value_list)

def isCSVFileEmpty():
    try:
        with open("clinicalTrialData.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            return countCSVRows(csv_reader) == 0
    except IOError:
        file = open("clinicalTrialData.csv", mode='w')
        file.close()
        return True

def countCSVRows(csv_reader):
    line_count = 0
    for row in csv_reader:
        if not row == []:
            line_count += 1
    return line_count
