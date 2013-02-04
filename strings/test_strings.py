import unittest
import strings

class TestStrings(unittest.TestCase):
    
    def test_get_string_length(self):
        self.assertEquals(strings.length(''), 0)
        self.assertEquals(strings.length('foo'), 3)
        
    def test_get_string_without(self):
        # implement strings.without that will remove given characters
        self.assertEquals(strings.without('abba', 'a'), 'bb')
        self.assertEquals(strings.without('abba', 'cd'), 'abba')
        self.assertEquals(strings.without('foobar', 'ob'), 'far')
        
    def test_count_discint_chars(self):
        # implement strings.count_distinct that will count the number of distinct characters
        self.assertEquals(strings.count_distinct('abba'), 2)
        self.assertEquals(strings.count_distinct('abcdfda'), 5)

    def test_tokens(self):
        # implement strings.tokens that will return a list of substrings split from . and removes empty tokens
        self.assertEquals(strings.tokens('foo.bar'), ['foo', 'bar'])
        self.assertEquals(strings.tokens('..foo..bar..'), ['foo', 'bar']) 
        self.assertEquals(strings.tokens('hello'), ['hello'])