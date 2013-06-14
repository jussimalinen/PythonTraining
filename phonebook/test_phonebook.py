import unittest
import os

import phonebook


class TestPhonebook(unittest.TestCase):
    
    def setUp(self):
        phonebook.clear()
    
    def test_add_name(self):
        phonebook.add("Eric Example", "+55 38 5588")
        
    def test_add_and_get(self):
        self._verify_add_and_get("Eric Example", "+55 123 456")
        self._verify_add_and_get("Maria", "358 44")
        self._verify_add_and_get("a", "1")

    def _verify_add_and_get(self, name, number):
        self.assertEquals(phonebook.add(name, number), True)
        self.assertEquals(phonebook.get(name), number)

    def test_get_non_existing_name(self):
        self._verify_number("Not there", "Unknown")
        
    def _verify_number(self, name, number):
        self.assertEquals(phonebook.get(name), number)

    def test_adding_illegal_numbers(self):
        self._verify_not_added("Illegal", "not valid")
        self._verify_not_added("Illegal", "123=12")
        self._verify_not_added("Illegal", "123 + 123")
        self._verify_not_added("Illegal", "")

    def test_adding_illegal_names(self):
        self._verify_not_added("Joe==Doe", "123")
        self._verify_not_added("Joe !#%&", "123")
        self._verify_not_added("", "123")

    def _verify_not_added(self, name, number):
        self.assertEquals(phonebook.add(name, number), False)
        self.assertEquals(phonebook.get(name), "Unknown")

    def test_clear(self):
        phonebook.add("name", "123")
        phonebook.clear()
        self._verify_number("name", "Unknown")
        
    def test_empty_book_to_string(self):
        self.assertEquals(phonebook._to_string(), "")
        
    def test_serialize_to_string(self):
        self._add_test_names()
        self.assertEquals(phonebook._to_string(), self.TEST_NAMES_SERIALIZED)
        
    def test_read_from_string(self):
        phonebook._read(self.TEST_NAMES_SERIALIZED)
        self._verify_test_names()
    
    def test_save_and_read_from_file(self):
        self._add_test_names()
        phonebook.save("test.temp")
        phonebook.clear()
        phonebook.load("test.temp")
        self._verify_test_names()
        os.remove("test.temp")

    TEST_NAMES_SERIALIZED="""John Doe=+555 123
Name=123
"""

    def _add_test_names(self):
        phonebook.add("Name", "123")
        phonebook.add("John Doe", "+555 123")

    def _verify_test_names(self):  
        self._verify_number("Name", "123")
        self._verify_number("John Doe", "+555 123")

if __name__ == "__main__":
    unittest.main()
