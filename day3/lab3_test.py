import unittest
import lab3_jh

class Lab3Test(unittest.TestCase):

	def test_shout(self):
		self.assertEqual("HELLO!", lab3_jh.shout("Hello").__str__())
		self.assertEqual("123!", lab3_jh.shout("123").__str__())
		self.assertEqual("ABC DEF QQ!", lab3_jh.shout("abC dEF qq").__str__())
		self.assertEqual("TEST!!", lab3_jh.shout("TEST!").__str__())
		
	def test_reverse(self):
		self.assertEqual("olleH", lab3_jh.reverse("Hello").__str__())
		self.assertEqual("tset tseT", lab3_jh.reverse("Test test").__str__())
		self.assertEqual("KcEhC 321", lab3_jh.reverse("123 ChEcK").__str__())
		
	def test_reverseword(self):
		self.assertEqual("world Hello", lab3_jh.reversewords("Hello world").__str__())
		self.assertEqual("!world Hello ?you are How", lab3_jh.reversewords("Hello world! How are you?").__str__())
		
		
if __name__ == '__main__':
	unittest.main()