import unittest
from unittest.mock import patch
from io import StringIO

from main_doc import (
    check_document_existance,
    get_doc_owner_name,
    get_all_doc_owners_names,
    remove_doc_from_shelf,
    add_new_shelf,
    append_doc_to_shelf,
    delete_doc,
    get_doc_shelf,
    move_doc_to_shelf,
    show_document_info,
    show_all_docs_info,
    add_new_doc
)

class TestAccountingFunctions(unittest.TestCase):

    def setUp(self):
        self.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        self.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

    def test_check_document_existance(self):
        self.assertTrue(check_document_existance("2207 876234"))
        self.assertTrue(check_document_existance("11-2"))
        self.assertTrue(check_document_existance("10006"))
        self.assertFalse(check_document_existance("12345"))

    @patch('builtins.input', return_value="2207 876234")
    def test_get_doc_owner_name(self, mock_input):
        expected_result = "Василий Гупкин"
        result = get_doc_owner_name()
        self.assertEqual(result, expected_result)

        mock_input.return_value = "12345"
        result = get_doc_owner_name()
        self.assertIsNone(result)

    def test_get_all_doc_owners_names(self):
        expected_result = {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}
        result = get_all_doc_owners_names()
        self.assertEqual(result, expected_result)

    def test_remove_doc_from_shelf(self):
        doc_number = "2207 876234"
        remove_doc_from_shelf(doc_number)
        self.assertNotIn(doc_number, self.directories['1'])

        doc_number = "12345"
        remove_doc_from_shelf(doc_number)
        self.assertNotIn(doc_number, self.directories['1'])

    @patch('builtins.input', side_effect=["4"])
    def test_add_new_shelf(self, mock_input):
        expected_result = ("4", True)
        result = add_new_shelf()
        self.assertEqual(result, expected_result)
        self.assertIn('4', self.directories)

        mock_input.return_value = "1"
        expected_result = ("1", False)
        result = add_new_shelf()
        self.assertEqual(result, expected_result)

    def test_append_doc_to_shelf(self):
        doc_number = "12345"
        shelf_number = "4"
        append_doc_to_shelf(doc_number, shelf_number)
        self.assertIn(doc_number, self.directories[shelf_number])

    @patch('builtins.input', return_value="2207 876234")
    def test_delete_doc(self, mock_input):
        expected_result = ("2207 876234", True)
        result = delete_doc()
        self.assertEqual(result, expected_result)
        self.assertNotIn("2207 876234", [doc['number'] for doc in self.documents])
        self.assertNotIn("2207 876234", self.directories.values())

        mock_input.return_value = "12345"
        expected_result = ("12345", None)
        result = delete_doc()
        self.assertEqual(result, expected_result)

    @patch('builtins.input', return_value="2207 876234")
    def test_get_doc_shelf(self, mock_input):
        expected_result = "1"
        result = get_doc_shelf()
        self.assertEqual(result, expected_result)

        mock_input.return_value = "12345"
        result = get_doc_shelf()
        self.assertIsNone(result)

    @patch('builtins.input', side_effect=["2207 876234", "2"])
    def test_move_doc_to_shelf(self, mock_input):
        move_doc_to_shelf()
        self.assertNotIn("2207 876234", self.directories['1'])
        self.assertIn("2207 876234", self.directories['2'])

        mock_input.side_effect = ["12345", "3"]
        move_doc_to_shelf()
        self.assertNotIn("12345", self.directories['1'])
        self.assertIn("12345", self.directories['3'])

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_document_info(self, mock_stdout):
        document = {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        show_document_info(document)
        expected_output = "passport \"2207 876234\" \"Василий Гупкин\"\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_all_docs_info(self, mock_stdout):
        show_all_docs_info()
        expected_output = "Список всех документов:\n\n" \
                          "passport \"2207 876234\" \"Василий Гупкин\"\n" \
                          "invoice \"11-2\" \"Геннадий Покемонов\"\n" \
                          "insurance \"10006\" \"Аристарх Павлов\"\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["123", "invoice", "John Doe", "4"])
    def test_add_new_doc(self, mock_input):
        expected_result = "4"
        result = add_new_doc()
        self.assertEqual(result, expected_result)
        self.assertEqual(len(self.documents), 4)
        self.assertIn("123", [doc['number'] for doc in self.documents])
        self.assertIn("123", self.directories['4'])

    def test_secretary_program_start(self):
        with patch('builtins.input', side_effect=["p", "2207 876234", "q"]):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                secretary_program_start()
                expected_output = "Введите номер документа - \n" \
                                  "\n" \
                                  "Владелец документа - Василий Гупкин\n" \
                                  "Введите команду - \n"
                self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
