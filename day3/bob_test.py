import unittest
from bob import Bob

class BobTest(unittest.TestCase):


	def test_on_say(self):
		self.assertEqual("Sure", Bob("Are you happy?").say().__str__())
		self.assertEqual("Woah, chill out!", Bob("HELLO!!!!!!!").say().__str__())
		self.assertEqual("Fine. Be that way!", Bob("").say().__str__())
		self.assertEqual("Whatever", Bob("I love you").say().__str__())
		
if __name__ == '__main__':
	unittest.main()
	