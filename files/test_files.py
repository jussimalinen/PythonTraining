import unittest
import files

class TestFiles(unittest.TestCase):
    
    def test_read_file_contents(self):
        self.assertEquals(files.read('test.txt'), 
"""Beautiful is better than ugly.
Explicit is better than implicit.""")
        self.assertEquals(len(files.read('zen.txt')), 856)

    def test_file_contains(self): 
        # implement files.contains that will check whether a file contains some text
        self.assertTrue(files.contains('better', 'test.txt'))
        self.assertFalse(files.contains('Hello', 'test.txt'))
        self.assertTrue(files.contains('a', 'zen.txt'))
        self.assertFalse(files.contains('invalid', 'test.txt'))

    def test_return_only_rows_starting_with(self):
        # implement files.file_rows_startingwith which will return only those rows from a file that start with some string
        self.assertEquals(files.file_rows_startingwith('Beautiful', 'test.txt'), 
"""Beautiful is better than ugly.
""")
        self.assertEquals(files.file_rows_startingwith('E', 'zen.txt'), 
"""Explicit is better than implicit.
Errors should never pass silently.
""")
