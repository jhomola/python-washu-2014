import unittest
from hw3_jh import *
from random import *

class hw3Test(unittest.TestCase):
	def setUp(self):
		self.unsorted1 = [uniform(-1000,1000) for i in xrange(1000)]
		self.unsorted2 = ["A", "c", "Q", "def", "zzz", "Hello", "23", "w0RLd", "qqq"]
		self.sorted1 = sorted(self.unsorted1)
		self.sorted2 = sorted(self.unsorted2)
		
	def test_selection(self):
		self.assertEqual(self.sorted1, selection_sort(self.unsorted1))
		self.assertEqual(self.sorted2, selection_sort(self.unsorted2))
		
	def test_merge(self):
		self.assertEqual(self.sorted1, merge_sort(self.unsorted1))
		self.assertEqual(self.sorted2, merge_sort(self.unsorted2))
		
	def test_quick(self):
		self.assertEqual(self.sorted1, quicksort(self.unsorted1, 0, len(self.unsorted1)-1))
		self.assertEqual(self.sorted2, quicksort(self.unsorted2, 0, len(self.unsorted2)-1))

		
if __name__ == '__main__':
	unittest.main()
