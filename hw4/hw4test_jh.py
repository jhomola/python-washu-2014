import unittest
from hw4_jh import *

class hw4Test(unittest.TestCase):
	def setUp(self):
		self.myList = LinkedList()
		self.myList.addNode(1)
		self.myList.addNode(2)
		self.myList.addNode(3)
		self.myList.addNode(4)
		self.myList.addNode(5)
		self.myList.addNode(6)
		self.myList.addNode(7)
		
	def test_length(self):
		self.assertEqual(self.myList.length, 7)
	
	def test_add(self):
		self.assertEqual(self.myList.head.value, 1)
		self.assertEqual(self.myList.head.next.next.value, 3)
		self.assertEqual(self.myList.head.next.next.next.next.value, 5)
		self.myList.addNodeAfter(33,3)
		self.assertEqual(self.myList.head.next.next.next.value, 33)
		self.myList.addNodeBefore(11,2)
		self.assertEqual(self.myList.head.next.value, 11)
	
	def test_remove(self):
		self.myList.removeNode(3)
		self.assertEqual(self.myList.head.next.next.value, 4)
		self.myList.removeNodesByValue(4)
		self.assertEqual(self.myList.head.next.next.value, 5)
		
	def test_reverse(self):
		self.assertEqual(self.myList.head.value, 1)
		self.assertEqual(self.myList.head.next.next.value, 3)
		self.assertEqual(self.myList.head.next.next.next.next.value, 5)
		self.myList.reverse()
		self.assertEqual(self.myList.head.value, 7)
		self.assertEqual(self.myList.head.next.next.value, 5)
		self.assertEqual(self.myList.head.next.next.next.next.value, 3)
		
		
if __name__ == '__main__':
	unittest.main()
