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
		self.assertEqual("G",self.firstRotor.getStartingKey())

		self.firstRotor.changeStartingKey(testKey2)
		self.assertEqual("Z",self.firstRotor.getStartingKey())

		self.secondRotor.changeStartingKey(testKey3)
		self.assertEqual("P",self.secondRotor.getStartingKey())

		self.firstRotor.changeStartingKey(testKey4)
		self.assertEqual("C",self.firstRotor.getStartingKey())


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
		
		self.assertEqual("Q",self.firstRotor.getStartingKey())

		self.firstRotor.increment()
		self.firstRotor.increment()
		self.firstRotor.increment()

		self.assertEqual("T",self.firstRotor.getStartingKey())


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
		self.firstRotor.changeStartingKey("Z")
		self.firstRotor.changeTurnoverKey("A")

		self.secondRotor.changeStartingKey("Z")
		self.secondRotor.changeTurnoverKey("A")

		self.thirdRotor.changeStartingKey("Z")
		self.thirdRotor.changeTurnoverKey("A")

		self.firstRotor.setNextRotor(self.secondRotor)
		self.secondRotor.setNextRotor(self.thirdRotor)

		self.secondRotor.setPreviousRotor(self.firstRotor)
		self.thirdRotor.setPreviousRotor(self.secondRotor)

		self.firstRotor.increment()

		self.assertEqual("A", self.firstRotor.encrypt("A"))
		self.assertEqual("A", self.secondRotor.encrypt("A"))
		self.assertEqual("A", self.thirdRotor.encrypt("A"))



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

		self.assertEqual("F",self.firstRotor.getStartingKey())
		self.firstRotor.reset()

		self.assertEqual("A",self.firstRotor.getStartingKey())




if __name__ == "__main__":
    unittest.main()

