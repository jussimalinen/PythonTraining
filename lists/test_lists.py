import unittest
import lst

class TestLists(unittest.TestCase):

	def test_sort_list(self):
		self.assertEquals(lst.sort(2,1,3,7), [1,2,3,7])
		self.assertEquals(lst.sort(2,-7), [-7,2])
		
	def test_find_largest_value(self):
		# implement lst.maximum (note that is should handle also numbers that are given as strings)
		self.assertEquals(lst.maximum(1,2,3,5,1), 5)
		self.assertEquals(lst.maximum('11',2,'3',5,1), 11)
		
	def test_only_positives(self):
		# implement lst.positives, which will return a list without negative numbers
		self.assertEquals(lst.positives(0, -5,-1,4), [0,4])
		self.assertEquals(lst.positives(-5,-11, -4), [])

if __name__ == "__main__":
    unittest.main()
