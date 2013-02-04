import unittest
import number

class TestArithmetics(unittest.TestCase):
    
    def test_add_two_number(self):
        self.assertEquals(number.add(1,2), 3)
        self.assertEquals(number.add(22,13), 35)

    def test_multiply(self):
        # implement number.multiply
        self.assertEquals(number.multiply(1,2), 2)
        self.assertEquals(number.multiply(10,2), 20)

    def test_safe_division(self):
        # implement number.divide, that will return 0 when you divide with 0.
        self.assertEquals(number.divide(4,2), 2)
        self.assertEquals(number.divide(7,3), 2)
        self.assertEquals(number.divide(7,0), 0)
        self.assertEquals(number.divide(0,0), 0)
        self.assertEquals(number.divide(0,3), 0)
                
    def test_add_many(self):
        # Modify number.add to add together any number of arguments
        self.assertEquals(number.add(1,2,3), 6)
        self.assertEquals(number.add(1,2,3,100,1000), 1106)
        
    def test_multiply_should_handle_strings(self):
        # Modify number.multiply to work also if arguments are given as strings
        self.assertEquals(number.multiply("2", "5"), 10)
        self.assertEquals(number.multiply(4, "5"), 20)
        
    def test_add_two_largest(self):
        # Implement number.add_two_largest, that adds up together two largest numbers in its arguments
        self.assertEquals(number.add_two_largest(6,1,2,10), 16)
        self.assertEquals(number.add_two_largest(1,1,10,1,10), 20)
