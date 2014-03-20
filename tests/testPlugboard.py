import unittest
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from plugboard import Plugboard

# Default mapping is
# WZ AB MO TF RX SG QU VI YN EL
class testPlugboard(unittest.TestCase):

	def setUp(self):
		self.plugboard = Plugboard()


	def test_changeString(self):
		testString = "WAMTRSQVYEcdz"
		self.assertEqual("ZBOFXGUINLCDZ",self.plugboard.changeString(testString))



if __name__ == "__main__":
    unittest.main()