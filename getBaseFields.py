import xml.etree.ElementTree as ET


class xmlFieldInterpreter():

    def __init__(self, xmlFile):
        # self.setRoot(xmlFile)
        self.tree = ET.parse(xmlFile)
        self.root = self.tree.getroot()
        # self.tree = ET.parse(self.CurrentxmlFileName)
        # self.root = self.tree.getroot()

    # def setRoot(self, xmlFileName):
    #     self.tree = ET.parse(xmlFileName)
    #     self.root = self.tree.getroot()
    #
    # def testPrint(self):
    #     for child in self.root:
    #         print(child.tag, child.text)

    def getNCTid(self):
        for child in self.root:
            if child.tag == "id_info":
                for grand_child in child:
                    if grand_child.tag == "nct_id":
                        return [grand_child.text, grand_child.tag]

    def getTopLevelFields(self):
        top_fields = []
        for child in self.root:
            current_child_info = [child.tag, child.text]
            top_fields.append(current_child_info)
        return top_fields

    def getFieldsWithID(self):
        id_info_pair = [self.getNCTid(), self.getTopLevelFields()]
        return id_info_pair
