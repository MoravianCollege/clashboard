from unittest import TestCase
import pytest
from getBaseFields import xmlFieldInterpreter

# testInterpreter = xmlFieldInterpreter

class TestXmlFieldInterpreter(TestCase):

    def test_makeXMLFieldInterpreter(self):
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")

    def test_getNCTID(self):
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        nct_id = test_interpreter.getNCTid()
        self.assertIsNotNone(nct_id)
        self.assertIsInstance(nct_id[0], str)

    def test_getDifferentNCTID(self):
        first_test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        first_nct_id = first_test_interpreter.getNCTid()
        second_test_interpreter = xmlFieldInterpreter("NCT00001308.xml")
        second_nct_id = second_test_interpreter.getNCTid()
        self.assertIsNot(first_nct_id, second_nct_id)

    def test_getBaseFields(self):
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        all_top_fields = test_interpreter.getTopLevelFields()
        self.assertIsNotNone(all_top_fields)

    def test_getIDFieldsPair(self):
        test_interpreter = xmlFieldInterpreter("NCT00001289.xml")
        nct_id = test_interpreter.getNCTid()
        all_top_fields = test_interpreter.getTopLevelFields()
        id_field_pair = test_interpreter.getFieldsWithID()
        self.assertIsNotNone(id_field_pair)
        self.assertEqual(nct_id, id_field_pair[0])
        self.assertEqual(all_top_fields, id_field_pair[1])
