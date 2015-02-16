# Test for rotor.py
import unittest
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from rotor import Rotor


class testRotor(unittest.TestCase):

	def setUp(self):
		self.firstRotor = Rotor()
		self.secondRotor = Rotor()
		self.thirdRotor = Rotor()


	def testChangeStartingKey(self):

		testKey1 = "G"
		testKey2 = "Z"
		testKey3 = "P"
		testKey4 = "c"

		self.firstRotor.changeStartingKey(testKey1)
		self.assertEqual("G",self.firstRotor.getCurrentKey())

		self.firstRotor.changeStartingKey(testKey2)
		self.assertEqual("Z",self.firstRotor.getCurrentKey())

		self.secondRotor.changeStartingKey(testKey3)
		self.assertEqual("P",self.secondRotor.getCurrentKey())

		self.firstRotor.changeStartingKey(testKey4)
		self.assertEqual("C",self.firstRotor.getCurrentKey())


	def testChangeTurnoverKey(self):

		testKey1 = "B"
		testKey2 = "H"
		testKey3 = "f"

		self.firstRotor.changeTurnoverKey(testKey1)
		self.assertEqual("B",self.firstRotor.getTurnoverKey())

		self.firstRotor.changeTurnoverKey(testKey2)
		self.assertEqual("H",self.firstRotor.getTurnoverKey())

		self.firstRotor.changeTurnoverKey(testKey3)
		self.assertEqual("F",self.firstRotor.getTurnoverKey())


	def testIncrement(self):

		testKey1 = "P"

		self.firstRotor.changeStartingKey(testKey1)
		self.firstRotor.changeTurnoverKey("B")
		self.firstRotor.increment()
		
		self.assertEqual("Q",self.firstRotor.getCurrentKey())

		self.firstRotor.increment()
		self.firstRotor.increment()
		self.firstRotor.increment()

		self.assertEqual("T",self.firstRotor.getCurrentKey())


	def testStaticStartingKey(self):

		testKey1 = "P"

		self.firstRotor.changeStartingKey(testKey1)
		self.firstRotor.increment()
		self.firstRotor.increment()
		self.firstRotor.increment()
		self.firstRotor.increment()
		self.firstRotor.increment()
		self.firstRotor.increment()

		self.assertEqual("P",self.firstRotor.getStaticStartingKey())



	def testSetNextRotor(self):

		self.firstRotor.setNextRotor(self.secondRotor)
		self.secondRotor.setNextRotor(self.thirdRotor)

		self.assertEqual(self.secondRotor, self.firstRotor.getNextRotor())
		self.assertEqual(self.thirdRotor, self.secondRotor.getNextRotor())


	def testSetPreviousRotor(self):

		self.secondRotor.setPreviousRotor(self.firstRotor)
		self.thirdRotor.setPreviousRotor(self.secondRotor)

		self.assertEqual(self.firstRotor,self.secondRotor.getPreviousRotor())
		self.assertEqual(self.secondRotor,self.thirdRotor.getPreviousRotor())



	def testEncrypt(self):


		# All three rotors should rotate
		self.firstRotor.changeStartingKey("O")
		self.firstRotor.changeTurnoverKey("Q")

		self.secondRotor.changeStartingKey("D")
		self.secondRotor.changeTurnoverKey("E")

		self.thirdRotor.changeStartingKey("A")
		self.thirdRotor.changeTurnoverKey("C")

		self.firstRotor.setNextRotor(self.secondRotor)
		self.secondRotor.setNextRotor(self.thirdRotor)

		self.secondRotor.setPreviousRotor(self.firstRotor)
		self.thirdRotor.setPreviousRotor(self.secondRotor)
	
		self.firstRotor.increment()
		# ADP
		self.assertEqual("P", self.firstRotor.encrypt("A"))
		self.assertEqual("D", self.secondRotor.encrypt("A"))
		self.assertEqual("A", self.thirdRotor.encrypt("A"))

		self.firstRotor.increment()
		# ADQ
		self.assertEqual("Q", self.firstRotor.encrypt("A"))
		self.assertEqual("D", self.secondRotor.encrypt("A"))
		self.assertEqual("A", self.thirdRotor.encrypt("A"))

		self.firstRotor.increment()
		# AER
		self.assertEqual("R", self.firstRotor.encrypt("A"))
		self.assertEqual("E", self.secondRotor.encrypt("A"))
		self.assertEqual("A", self.thirdRotor.encrypt("A"))

		self.firstRotor.increment()
		# BFS
		self.assertEqual("S", self.firstRotor.encrypt("A"))
		self.assertEqual("F", self.secondRotor.encrypt("A"))
		self.assertEqual("B", self.thirdRotor.encrypt("A"))

		self.firstRotor.increment()
		# BFT
		self.assertEqual("T", self.firstRotor.encrypt("A"))
		self.assertEqual("F", self.secondRotor.encrypt("A"))
		self.assertEqual("B", self.thirdRotor.encrypt("A"))



	def testPostEncrypt(self):

		self.firstRotor.changeStartingKey("A")
		self.secondRotor.changeStartingKey("A")
		self.thirdRotor.changeStartingKey("A")

		self.assertEqual("A", self.firstRotor.postEncrypt("A"))
		self.assertEqual("A", self.secondRotor.postEncrypt("A"))
		self.assertEqual("A", self.thirdRotor.postEncrypt("A"))


	def testReset(self):

		self.firstRotor.changeStartingKey("A")
		self.firstRotor.changeTurnoverKey("Z")

		self.firstRotor.increment()
		self.firstRotor.increment()
		self.firstRotor.increment()
		self.firstRotor.increment()
		self.firstRotor.increment()

		self.assertEqual("F",self.firstRotor.getCurrentKey())
		self.firstRotor.reset()

		self.assertEqual("A",self.firstRotor.getCurrentKey())




if __name__ == "__main__":
    unittest.main()

